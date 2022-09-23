from django import forms
from .models import InCityObject


class InCitySearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_region'].initial = 2
        self.fields['object_type'].initial = 2
        self.fields['rooms'].initial = 2

    class Meta:
        model = InCityObject
        fields = ('sale_or_rent', 'object_type', 'city_region', 'rooms')
