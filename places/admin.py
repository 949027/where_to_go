from django.contrib import admin
from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', )


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
admin.site.register(Place, PlaceAdmin)
