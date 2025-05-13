from django.urls import path
from core.views import cargo_create, cargo_list,cargo_update,cargo_delete
from core.views import departamento_create, departamento_list,departamento_update,departamento_delete
from core.views import empleado_create, empleado_list,empleado_update,empleado_delete
from core.views import rol_create, rol_list,rol_update,rol_delete
from core.views import tipoContrato_create, tipoContrato_list,tipoContrato_update,tipoContrato_delete
from core.views import rol_delete
from . import views

app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    
    path('signup/', views.signup, name='signup'),  # URL for the signup view
    path('logout/', views.signout, name='logout'),  # URL for the logout view
    path('signin/', views.signin, name='signin'),  # URL for the signin view
    
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

    path('empleado_list/', empleado_list, name='empleado_list'),  # URL para la vista home
    path('empleado_create/', empleado_create, name='empleado_create'),  # URL para la vista home
    path('empleado_update/<int:id>', empleado_update, name='empleado_update'),  # URL para la vista home
    path('empleado_delete/<int:id>', empleado_delete, name='empleado_delete'),  # URL para la vista home

    path('rol_list/', rol_list, name='rol_list'),  # URL para la vista home
    path('rol_create/', rol_create, name='rol_create'),  # URL para la vista home
    path('rol_update/<int:id>', rol_update, name='rol_update'),  # URL para la vista home
    path('rol_delete/<int:id>', rol_delete, name='rol_delete'),  # URL para la vista home
    
    
    

]