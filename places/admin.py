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
        image_width = 200
        image_height = obj.file.height * image_width / obj.file.width
        return format_html(
            '<img src="{}" width="{}" height={} />',
            obj.file.url,
            image_width,
            image_height,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    search_fields = ('title', )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
