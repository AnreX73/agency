from django.urls import path

from agency.views import *

urlpatterns = [
    path('', index, name='home'),
    # path('apartment/', showApartment, name='show_apartment'),
 ]