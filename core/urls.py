from django.urls import path
from core.views import cargo_create, cargo_list,cargo_update,cargo_delete

app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('cargo_list/', cargo_list, name='cargo_list'),  # URL para la vista home
    path('cargo_create/', cargo_create, name='cargo_create'),  # URL para la vista home
    path('cargo_update/<int:id>', cargo_update, name='cargo_update'),  # URL para la vista home
    path('cargo_delete/<int:id>', cargo_delete, name='cargo_delete'),  # URL para la vista home

]