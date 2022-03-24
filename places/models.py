from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    description_short = models.TextField(
        'Краткое описание',
        max_length=400,
        blank=True
    )
    description_long = HTMLField('Подробное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField('Номер', blank=True)
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    file = models.ImageField('Изображения')

    def __str__(self):
        return f'{self.number} {self.place}'

    class Meta(object):
        ordering = ['number']
