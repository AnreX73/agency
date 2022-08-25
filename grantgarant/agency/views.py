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
        'apartments': InCityObject.objects.filter(object_type__title='Квартира').order_by('-time_create'),
        'apartments_icon': Graphics.objects.get(description='иконка квартир'),
        'new_apartments': InCityObject.objects.filter(object_type__title='Новостройка').order_by('-time_create'),
        'new_apartments_icon': Graphics.objects.get(description='иконка новостроек'),
        'mini_apartments': InCityObject.objects.filter(object_type__title='Комната').order_by('-time_create'),
        'mini_apartments_icon': Graphics.objects.get(description='иконка комнаты'),

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
