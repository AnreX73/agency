from django import template

from agency.models import *

register = template.Library()


@register.inclusion_tag('agency/header.html')
def show_header():
    contacts = Contacts.objects.all()
    logo = Graphics.objects.get(note='logo')
    phone_icon = Graphics.objects.get(description='иконка телефона')
    catalog_link = 'каталог'
    return {"contacts": contacts,
            "logo": logo,
            "catalog_link":catalog_link,
            'phone_icon': phone_icon,
            }


@register.inclusion_tag('agency/nav.html')
def show_nav():
    in_city_object_type = InCityObjectType.objects.all()
    out_city_object_type = OutCityObjectType.objects.all()
    
    return{
        'in_city_object_type':in_city_object_type,
        'out_city_object_type':out_city_object_type 
           
    }
    
