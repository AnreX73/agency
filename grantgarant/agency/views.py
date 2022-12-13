from multiprocessing.sharedctypes import Value
from django.shortcuts import render, get_object_or_404

from agency.forms import InCitySearchForm
from agency.models import *


def index(request):
    context = {
        'title': 'Агенство ЕЦН',
        'main_page_img': Graphics.objects.get(description='изображение на главную'),
        'main_page_slogan': Graphics.objects.get(description='Слоган'),
        'hot_city_obj': InCityObject.objects.filter(is_hot=True).filter(sale_or_rent='s').order_by('-time_create'),
        'hot_out_city_obj': OutCityObject.objects.filter(is_hot=True).order_by('-time_create'),
        'hot_title': Graphics.objects.get(description='горячая кнопка на главной'),
        'no_photo': Graphics.objects.get(description='нет фото'),
        'services': Post.objects.all(),
    }
    return render(request, 'agency/index.html', context=context)


def show_apartments(request, obj_type_slug):
    apartments_type = get_object_or_404(InCityObjectType, slug=obj_type_slug)
    unselected_links = InCityObjectType.objects.exclude(slug=obj_type_slug)
   
    context = {
        'apartments_type': apartments_type,
        'unselected_links': unselected_links,
        'search_icon' : Graphics.objects.get(description='иконка поиска'),

    }
    return render(request, 'agency/show_apartments.html', context=context)


def show_dachas(request, obj_type_slug):
    dachas_type = get_object_or_404(OutCityObjectType, slug=obj_type_slug)
    unselected_links = OutCityObjectType.objects.exclude(slug=obj_type_slug)
    context = {
        'dachas_type': dachas_type,
        'unselected_links': unselected_links,

    }
    return render(request, 'agency/show_dachas.html', context=context)


def show_rent(request, obj_type_slug):
    rent_obj_type = get_object_or_404(InCityObjectType, slug=obj_type_slug)
    unselected_links = InCityObjectType.objects.exclude(slug=obj_type_slug)
    context = {
        'rent_obj_type': rent_obj_type,
        'unselected_links': unselected_links,

    }
    return render(request, 'agency/show_rent.html', context=context)


def show_apartment(request, apartment_slug):
    apartment = get_object_or_404(InCityObject, slug=apartment_slug)
    apartment_id = apartment.id
    context = {
        'apartment': apartment,
        'gallery': Gallery.objects.filter(galleryLink_id=apartment_id),
        'no_photo': Graphics.objects.get(description='нет фото')
    }
    return render(request, 'agency/apartment.html', context=context)


def show_dacha(request, dacha_slug):
    dacha = get_object_or_404(OutCityObject, slug=dacha_slug)
    dacha_id = dacha.id
    context = {
        'dacha': dacha,
        'gallery': Gallery2.objects.filter(galleryLink2_id=dacha_id),
        'no_photo': Graphics.objects.get(description='нет фото')
    }
    return render(request, 'agency/dacha.html', context=context)


def searched_obj(request):
    if request.method == 'POST':
        form = InCitySearchForm(request.POST)
        if form.is_valid():
            try:
                obj_dic = {k: v for k, v in form.cleaned_data.items() if v is not None}
                selected_items = InCityObject.objects.filter(**obj_dic).filter(is_published=True)
              
                print(selected_items)


            except:
                form.add_error(None, 'ERROR')

    else:
        selected_items = InCityObject.objects.filter(sale_or_rent='s')  
        form = InCitySearchForm()
    context = {
        'title': 'Агенство ЕЦН - поиск',
        'form': form,
        'selected_items': selected_items,
        'no_photo': Graphics.objects.get(description='нет фото'),
       

    }
    return render(request, 'agency/searched_obj.html', context=context)
