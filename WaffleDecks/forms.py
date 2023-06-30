from django import forms
from .models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Este es el formulario que permite registrar.


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    region = forms.CharField(
        widget=forms.Select(attrs={'id': 'select-region'}))
    comuna = forms.CharField(
        widget=forms.Select(attrs={'id': 'select-comuna'}))
    direccion = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'region',
                  'comuna', 'direccion', 'password1', 'password2')
