from django import template

from agency.models import Contacts, Graphics

register = template.Library()


@register.inclusion_tag('agency/header.html')
def show_header():
    contacts = Contacts.objects.all()
    logo = Graphics.objects.get(note='logo')
    contact_link = 'контакты'
    return {"contacts": contacts,
            "logo": logo,
            "contact_link ": contact_link,
            }
