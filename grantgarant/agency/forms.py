from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=150,
                               widget=forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 1}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
