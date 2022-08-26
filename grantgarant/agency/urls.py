from django.urls import path

from agency.views import *

urlpatterns = [
    path('', index, name='home'),
    path('apartments/', apartments, name='apartments'),
    path('show_apartment/<slug:apartment_slug>',show_apartment, name='show_apartment'),
    path('dacha/', dacha, name='dacha'),
    path('show_dacha/<slug:dacha_slug>',show_dacha, name='show_dacha'),

 ]