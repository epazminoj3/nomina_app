from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select, DateInput
from django import forms
from .models import Cargo
from .models import Departamento
from .models import Empleado
from .models import Rol
from .models import TipoContrato
from django import forms
from .models import Rol 



class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion'].strip().capitalize()
        if Cargo.objects.filter(descripcion__iexact=descripcion).exists():
            raise forms.ValidationError("Este cargo ya existe.")
        return descripcion



class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion'].strip().capitalize()
        if Departamento.objects.filter(descripcion__iexact=descripcion).exists():
            raise forms.ValidationError("Este departamento ya existe.")
        return descripcion



class TipoContratoForm(forms.ModelForm):

    class Meta:
        model = TipoContrato
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion'].strip().capitalize()
        if TipoContrato.objects.filter(descripcion__iexact=descripcion).exists():
            raise forms.ValidationError("Este tipo de contrato ya existe.")
        return descripcion

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
        }
    


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'aniomes': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas_extras': forms.NumberInput(attrs={'class': 'form-control'}),
            'bono': forms.NumberInput(attrs={'class': 'form-control'}),
            'iess': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tot_ing': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tot_des': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'neto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        


