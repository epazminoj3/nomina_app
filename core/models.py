from django.db import models

# Create your models here.
from django.db import models 
 
class Cargo(models.Model): 
    descripcion = models.CharField(max_length=100) 
 
class Departamento(models.Model): 
    descripcion = models.CharField(max_length=100) 
 
class TipoContrato(models.Model): 
    descripcion = models.CharField(max_length=100) 
 
class Empleado(models.Model): 
    SEXO_CHOICES = [ 
        ('M', 'Masculino'), 
        ('F', 'Femenino'), 
    ] 
     
    nombre = models.CharField(max_length=100) 
    cedula = models.CharField(max_length=20, unique=True) 
    direccion = models.TextField() 
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES) 
    sueldo = models.DecimalField(max_digits=10, decimal_places=2) 
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE) 
    departamento = models.ForeignKey(Departamento, 
on_delete=models.CASCADE) 
    tipo_contrato = models.ForeignKey(TipoContrato, 
on_delete=models.CASCADE) 
 
class Rol(models.Model): 
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) 
    aniomes = models.DateField()#202501 
    sueldo = models.DecimalField(max_digits=10, decimal_places=2) 
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2) 
    bono = models.DecimalField(max_digits=10, decimal_places=2) 
    iess = models.DecimalField(max_digits=10, decimal_places=2)  
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2) 
    tot_des = models.DecimalField(max_digits=10, decimal_places=2) 
    neto = models.DecimalField(max_digits=10, decimal_places=2) 