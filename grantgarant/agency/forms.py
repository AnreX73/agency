from django import forms
from .models import InCityObject, OutCityObject


class InCitySearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_region'].empty_label = 'все районы'
        self.fields['object_type'].empty_label = 'все предложения'
        self.fields['rooms'].empty_label = 'все предложения'
        self.fields['rooms'].required = False
        self.fields['city_region'].required = False
        self.fields['object_type'].required = False


    class Meta:
        model = InCityObject
        fields = ('sale_or_rent', 'object_type', 'city_region', 'rooms')
