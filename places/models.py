from django.db import models

class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    imgs = models.ImageField('Изображения')
    description_short = models.CharField('Краткое описание', max_length=200)
    description_long = models.TextField('Подробное описание')
    lng = models.FloatField()
    lat = models.FloatField()
