from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    context = {
        'title': 'Грант Гарант',
        'cityObjects': InCityObject.objects.all(),
        'outcityObjects': OutCityObject.objects.all(),
        

    }
    return render(request, 'agency/index.html', context=context)
