from multiprocessing.sharedctypes import Value
from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    context = {
        'title': 'Агенство Грант Гарант',
        'main_page_img': Graphics.objects.get(description='изображение на главную'),
        'main_page_slogan': Graphics.objects.get(description='Слоган'),
        'main_page_hot_button': Graphics.objects.get(description='горячая кнопка на главной'),

    }
    return render(request, 'agency/index.html', context=context)


def apartments(request):
    context = {
        'apartments_icon': InCityObjectType.objects.get(title='Квартиры'),
        'new_apartments_icon': InCityObjectType.objects.get(title='Новостройки'),
        'mini_apartments_icon': InCityObjectType.objects.get(title='Комнаты'),
    }
    return render(request, 'agency/apartments.html', context=context)


def dacha(request):
    context = {
        'dacha_icon': Graphics.objects.get(description='иконка загородной недвижимости'),
        'cottage_icon': Graphics.objects.get(description='иконка коттеджа'),
        'land_icon': Graphics.objects.get(description='иконка земельного участка'),
    }
    return render(request, 'agency/dachas.html', context=context)


def show_apartment(request, apartment_slug):
    apartment = get_object_or_404(InCityObject, slug=apartment_slug)
    apartment_id = apartment.id
    context = {
        'apartment': apartment,
        'gallery': Gallery.objects.filter(galleryLink_id=apartment_id)
    }
    return render(request, 'agency/apartment.html', context=context)


def show_dacha(request, dacha_slug):
    dacha = get_object_or_404(OutCityObject, slug=dacha_slug)
    dacha_id = dacha.id
    context = {
        'dacha': dacha,
        'gallery': Gallery2.objects.filter(galleryLink2_id=dacha_id)

    }
    return render(request, 'agency/dacha.html', context=context)
