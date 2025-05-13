from django.contrib import admin

from .models import Cargo, Departamento, Empleado, Rol, TipoContrato

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
admin.site.register(Empleado)
admin.site.register(Rol)
