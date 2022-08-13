from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    context = {
        'title': 'Грант Гарант',
        'cityObjects': InCityObject.objects.filter(rooms__title='3 - комнатная').filter(metro__title='Заельцовская'),
        'outcityObjects': OutCityObject.objects.all(),

    }
    return render(request, 'agency/index.html', context=context)


# def showApartment(request, apartment_slug):
#     apartment = get_object_or_404(InCityObject, slug=apartment_slug)
#     context = {
#         'apartment': apartment,
#         'title': apartment.title,
#         'services': Services.objects.filter(cat_id=1),
#         'souvenirs': Services.objects.filter(cat_id=2),
#         'gallery': Gallery.objects.all(),
#         'prices': Prices.objects.all(),
#         'extracontent': Extra.objects.all(),
#     }
#     return render(request, 'agency/apartment.html', context=context)
