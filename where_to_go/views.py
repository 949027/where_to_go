from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from places.models import Place


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response_data = {
        "title": place.title,
        "imgs": [image.file.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
            }
        }
    return JsonResponse(
        response_data,
        json_dumps_params={'ensure_ascii': False, 'indent': 2},
    )


def index(request):
    features = []
    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse(show_place, args=[place.id]),
            }
        }
        features.append(feature)

    context = {'places': {
        "type": "FeatureCollection",
        "features": features,
    }}
    return render(request, 'index.html', context=context)
