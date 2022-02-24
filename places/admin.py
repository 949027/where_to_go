from django.contrib import admin
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)


admin.site.register(Place, PlaceAdmin)

