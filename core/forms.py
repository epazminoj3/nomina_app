from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from .models import Cargo
class CargoForm(ModelForm):

    class Meta:
        model = Cargo
        fields = '__all__'
        # exclude = ['phone']

        widgets = {
            'description': TextInput(attrs={'class': 'form-control'}),
            # No incluimos specialty aquí porque ya lo definimos arriba
        }