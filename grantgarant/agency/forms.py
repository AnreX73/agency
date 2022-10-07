from django import forms
from .models import InCityObject, OutCityObject


class InCitySearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_region'].empty_label = 'не выбрано'
        self.fields['object_type'].empty_label = 'не выбрано'
        self.fields['rooms'].empty_label = 'не выбрано'

    class Meta:
        model = InCityObject
        fields = ('sale_or_rent', 'object_type', 'city_region', 'rooms')


