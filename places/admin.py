from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [
        'headshot_image',
    ]

    def headshot_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" height={} />',
            obj.file.url,
            200,
            obj.file.height * 200 / obj.file.width,
        )


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    search_fields = ('title', )
    inlines = [
        ImageInline,
    ]


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Place, PlaceAdmin)
