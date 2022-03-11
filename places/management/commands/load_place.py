import os
from urllib.parse import urlparse
import requests
from progress.bar import Bar
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('link', type=str)

    def handle(self, *args, **options):
        link = options['link']
        response = requests.get(link)
        response.raise_for_status()
        place_data = response.json()
        place, _ = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            lng=place_data['coordinates']['lng'],
            lat=place_data['coordinates']['lat'],
        )

        images_urls = place_data['imgs']
        bar = Bar('Loading photo...', max=len(images_urls))

        for number, image_url in enumerate(images_urls):
            try:
                response = requests.get(image_url)
                response.raise_for_status()

                image_content = ContentFile(response.content)
                image_path = urlparse(image_url).path
                image_name = os.path.basename(image_path)
                image, _ = Image.objects.get_or_create(
                    number=number,
                    place=place,
                )
                image.file.save(image_name, image_content, save=True)
                bar.next()
            except requests.HTTPError as err:
                print(err)

        bar.finish()
