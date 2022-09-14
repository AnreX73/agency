from django import template

from agency.models import *

register = template.Library()


@register.inclusion_tag('agency/inclusion/header.html')
def show_header():
    contacts = Contacts.objects.filter(extra_description='тел.' )
    logo = Graphics.objects.get(note='logo')
    phone_icon = Graphics.objects.get(description='иконка телефона')
    in_city_object_type = InCityObjectType.objects.filter(in_main_page=True)
    out_city_object_type = OutCityObjectType.objects.filter(in_main_page=True)
    return {"contacts": contacts,
            "logo": logo,
            'phone_icon': phone_icon,
            'in_city_object_type': in_city_object_type,
            'out_city_object_type': out_city_object_type
            }


@register.inclusion_tag('agency/inclusion/items_list.html')
def show_apa(obj_list_type='city', obj_type='vtorichnoe-zhile'):
    if obj_list_type == 'city':
        selected_items = InCityObject.objects.filter(object_type__slug=obj_type).filter(is_for_sale=True).order_by('-time_create')
        incity_id = InCityObjectType.objects.get(slug=obj_type)
         
    else:
        selected_items = OutCityObject.objects.filter(object_type__slug=obj_type).filter(is_for_sale=True).order_by('-time_create')
        incity_id = OutCityObjectType.objects.get(slug=obj_type)
    return {
        'selected_items': selected_items,
        'incity_id':incity_id 
    }

