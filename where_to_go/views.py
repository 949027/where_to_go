from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from places.models import Place


def show_place(request, placeId):
    place = get_object_or_404(Place, placeId=placeId)
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
                "placeId": place.placeId,
                "detailsUrl": reverse(show_place, args=[place.placeId]),
            }
        }
        features.append(feature)

    context = {'places': {
        "type": "FeatureCollection",
        "features": features,
    }}
    return render(request, 'index.html', context=context)
