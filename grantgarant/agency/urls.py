from django.urls import path

from agency.views import *

urlpatterns = [
    path('', index, name='home'),
    path('searched_obj/', searched_obj, name='searched_obj'),
    path('show_apartments/<slug:obj_type_slug>', show_apartments, name='show_apartments'),
    path('room_amount/<slug:rooms_slug>', room_amount, name='room_amount'),
    path('show_dachas/<slug:obj_type_slug>', show_dachas, name='show_dachas'),
    path('show_rent/<slug:obj_type_slug>', show_rent, name='show_rent'),
    path('show_apartment/<slug:apartment_slug>', show_apartment, name='show_apartment'),
    path('show_dacha/<slug:dacha_slug>', show_dacha, name='show_dacha'),

]
