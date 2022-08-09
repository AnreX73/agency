from django.shortcuts import render, get_object_or_404

from agency.models import *


def index(request):
    context = {
        'title': 'СМАРТ ФОТО',

    }
    return render(request, 'agency/index.html', context=context)
