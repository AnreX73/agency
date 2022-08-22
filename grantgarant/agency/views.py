from multiprocessing.sharedctypes import Value
from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    
    context = {
        'title': 'Агенство Грант Гарант',
        'main_page_img': Graphics.objects.get(description='изображение на главную'),
        'main_page_slogan': Graphics.objects.get(description='Слоган'),
        'main_page_hot_button': Graphics.objects.get(description='горячая кнопка на главной'),
        'in_city_object_type': InCityObjectType.objects.all(),
        'out_city_object_type': OutCityObjectType.objects.all(),
    }
    return render(request, 'agency/index.html', context=context)


def apartments(request):
    context = {
        'apartments': InCityObject.objects.all(),
        'grath': Graphics.objects.get(description='иконка квартир')
    }
    return render(request, 'agency/apartments.html', context=context)


def show_apartment(request, apartment_slug):
    apartment = get_object_or_404(InCityObject, slug=apartment_slug)
    apartment_id = apartment.id
    context = {
        'apartment': apartment,
        'gallery': Gallery.objects.filter(galleryLink_id=apartment_id)

    }
    return render(request, 'agency/apartment.html', context=context)
