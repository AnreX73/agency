from django import forms
from .models import InCityObject


class SearchForm(forms.ModelForm):
    class Meta:
        model = InCityObject
        fields = '__all__'
