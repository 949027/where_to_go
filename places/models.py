from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    description_short = models.CharField('Краткое описание', max_length=400)
    description_long = HTMLField('Подробное описание')
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField('Номер')
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    file = models.ImageField('Изображения', blank=True)

    def __str__(self):
        return f'{self.number} {self.place}'

    class Meta(object):
        ordering = ['number']
