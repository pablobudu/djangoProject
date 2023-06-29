from django import forms
from .models import Usuario
from django.forms import ModelForm


class RegistroUsuarioForm(ModelForm):
    region = forms.CharField(
        widget=forms.Select(attrs={'id': 'select-region'}))
    comuna = forms.CharField(
        widget=forms.Select(attrs={'id': 'select-comuna'}))

    class Meta:
        model = Usuario
        fields = "__all__"
