from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from .models import Cargo
from .models import Departamento
class CargoForm(ModelForm):

    class Meta:
        model = Cargo
        fields = '__all__'

        widgets = {
            'description': TextInput(attrs={'class': 'form-control'}),
        }

class DepartamentoForm(ModelForm):

    class Meta:
        model = Departamento
        fields = '__all__'
       

        widgets = {
            'description': TextInput(attrs={'class': 'form-control'}),
           
        }