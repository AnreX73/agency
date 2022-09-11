from django import forms
from .models import InCityObject


class SearchForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['object_type'].empty_label = 'Не выбрано'
        self.fields['city_region'].empty_label = 'Не выбрано'
        self.fields['rooms'].empty_label = 'Не выбрано'

    class Meta:
        model = InCityObject
        fields = ('object_type','city_region','rooms')
