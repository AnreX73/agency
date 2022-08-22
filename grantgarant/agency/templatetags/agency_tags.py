from django import template

from agency.models import Contacts, Graphics

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
