from multiprocessing.sharedctypes import Value
from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    context = {
        'title': 'Грант Гарант',
        'cityObjects': InCityObject.objects.filter(rooms__title='3 - комнатная').filter(metro__title='Заельцовская'),
        'outcityObjects': OutCityObject.objects.all(),

    }
    return render(request, 'agency/index.html', context=context)


def apartments(request):
    context = {
        'apartments': InCityObject.objects.all(),
        'grath': Graphics.objects.get(note='квартиры и комнаты')
    }
    return render(request, 'agency/apartments.html', context=context)


def show_apartment(request, apartment_slug):
    apartment = get_object_or_404(InCityObject, slug=apartment_slug)
    context = {
        'apartment': apartment,
        
    }
    return render(request, 'agency/apartment.html', context=context)
