from django import forms
from .models import InCityObject


class InCitySearchForm(forms.ModelForm):
    sale_or_rent = forms.ChoiceField(choices=((1, 'Продажа'), (2, 'Аренда')), label='Продажа или аренда', initial=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['object_type'].initial = 2
        self.fields['city_region'].initial = 2
        self.fields['rooms'].initial = 2

    field_order = ["sale_or_rent", ]

    class Meta:
        model = InCityObject
        fields = ('object_type', 'city_region', 'rooms')
