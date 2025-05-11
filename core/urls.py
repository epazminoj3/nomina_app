from django.urls import path
from core.views import cargo_create, cargo_list,cargo_update,cargo_delete
from core.views import departamento_create, departamento_list,departamento_update,departamento_delete
from core.views import tipoContrato_create, tipoContrato_list,tipoContrato_update,tipoContrato_delete

app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('cargo_list/', cargo_list, name='cargo_list'),  # URL para la vista home
    path('cargo_create/', cargo_create, name='cargo_create'),  # URL para la vista home
    path('cargo_update/<int:id>', cargo_update, name='cargo_update'),  # URL para la vista home
    path('cargo_delete/<int:id>', cargo_delete, name='cargo_delete'),  # URL para la vista home

    path('departamento_list/', departamento_list, name='departamento_list'),  # URL para la vista home
    path('departamento_create/', departamento_create, name='departamento_create'),  # URL para la vista home
    path('departamento_update/<int:id>', departamento_update, name='departamento_update'),  # URL para la vista home
    path('departamento_delete/<int:id>', departamento_delete, name='departamento_delete'),  # URL para la vista home

    path('tipoContrato_list/', tipoContrato_list, name='tipoContrato_list'),  # URL para la vista home
    path('tipoContrato_create/', tipoContrato_create, name='tipoContrato_create'),  # URL para la vista home
    path('tipoContrato_update/<int:id>', tipoContrato_update, name='tipoContrato_update'),  # URL para la vista home
    path('tipoContrato_delete/<int:id>', tipoContrato_delete, name='tipoContrato_delete'),  # URL para la vista home



]