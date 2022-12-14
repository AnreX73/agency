from django.urls import path

from agency.views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('searched_obj/', searched_obj, name='searched_obj'),
    path('show_apartments/<slug:obj_type_slug>', show_apartments, name='show_apartments'),
    path('show_dachas/<slug:obj_type_slug>', show_dachas, name='show_dachas'),
    path('show_rent/<slug:obj_type_slug>', show_rent, name='show_rent'),
    path('show_apartment/<slug:apartment_slug>', show_apartment, name='show_apartment'),
    path('show_dacha/<slug:dacha_slug>', show_dacha, name='show_dacha'),


]
