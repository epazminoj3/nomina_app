from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from .models import Cargo
from .models import Departamento
from .models import TipoContrato
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
        
class TipoContratoForm(ModelForm):

    class Meta:
        model = TipoContrato
        fields = '__all__'
       

        widgets = {
            'description': TextInput(attrs={'class': 'form-control'}),
           
        }