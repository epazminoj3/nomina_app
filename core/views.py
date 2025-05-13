from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from core.models import Cargo, Departamento, Empleado, Rol, TipoContrato
from core.forms import CargoForm, DepartamentoForm, EmpleadoForm, RolForm, TipoContratoForm
from .forms import RolForm
from .models import Empleado
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    data = {
        'title': 'App Nominas',
        'description': 'Nominas de empleados',
        'author': 'Erick Pazmiño-Maykel Aroca',
        'year': 2025,
    }
    return render(request, 'home.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                messages.success(request, '¡Usuario registrado exitosamente!')
                return redirect('home') 
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya existe. Elige otro.')
                return render(request, 'signup.html', {
                    'form': UserCreationForm
                })
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'signup.html', {
                'form': UserCreationForm
            })

        

def signout(request):
    logout(request)
    return redirect('home')    

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos.'
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
## Vista para la lista de cargos
def cargo_list(request):
    query = request.GET.get('q', None)
    if query:
        cargos_list = Cargo.objects.filter(descripcion__icontains=query)
    else:
        cargos_list = Cargo.objects.all().order_by('id')  # Ordenamos por id
    
    # Configuración de paginación (mostrar 5 elementos por página)
    paginator = Paginator(cargos_list, 5)
    page_number = request.GET.get('page')
    cargos = paginator.get_page(page_number)
    
    context = {
        'cargos': cargos,
        'title': 'Listado de cargos',
        'query': query  # Pasamos la query para mantenerla en la paginación
    }
    return render(request, 'cargo/list.html', context)


@login_required
def cargo_create(request):
    context={'title':'Ingresar Cargo'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")

        form = CargoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'cargo/create.html', context)
    else:
        #  print("entro por post")
        form = CargoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # cargo = form.save(commit=False)# lo tiene en memoria
            # cargo.user = request.user
            # cargo.save() # lo guarda en la BD
            return redirect('core:cargo_list')
        else:
            context['form'] = form
            return render(request, 'cargo/create.html',context)

@login_required
def cargo_update(request,id):
   context={'title':'Actualizar Cargo'}
   cargo = Cargo.objects.get(pk=id)
   if request.method == "GET":
      form = CargoForm(instance=cargo)# instancia el formulario con los datos del cargo
      context['form'] = form
      return render(request, 'cargo/create.html', context)
   else:
      form = CargoForm(request.POST,instance=cargo)
      if form.is_valid():
          form.save()
          return redirect('core:cargo_list')
      else:
          context['form'] = form
          return render(request, 'cargo/create.html', context)

@login_required
def cargo_delete(request, id):
    cargo = get_object_or_404(Cargo, pk=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect('core:cargo_list')
    return render(request, 'delete/confirm_delete.html', {
        'object': cargo,
        'object_name': 'cargo',
        'cancel_url': reverse('core:cargo_list')
    })


@login_required
## Vista para la lista de departamentos
def departamento_list(request):
    query = request.GET.get('q', None)
    if query:
        departamentos_list = Departamento.objects.filter(descripcion__icontains=query)
    else:
        departamentos_list = Departamento.objects.all().order_by('id')
    
    paginator = Paginator(departamentos_list, 5)
    page_number = request.GET.get('page')
    departamentos = paginator.get_page(page_number)
    
    context = {
        'departamentos': departamentos,
        'title': 'Listado de departamentos',
        'query': query
    }
    return render(request, 'departamento/list.html', context)


@login_required
def departamento_create(request):
    context={'title':'Ingresar Departamento'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")

        form = DepartamentoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'departamento/create.html', context)
    else:
        #  print("entro por post")
        form = DepartamentoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # cargo = form.save(commit=False)# lo tiene en memoria
            # cargo.user = request.user
            # cargo.save() # lo guarda en la BD
            return redirect('core:departamento_list')
        else:
            context['form'] = form
            return render(request, 'departamento/create.html',context)

@login_required
def departamento_update(request,id):
   context={'title':'Actualizar Departamento'}
   departamento = Departamento.objects.get(pk=id)
   if request.method == "GET":
      form = DepartamentoForm(instance=departamento)# instancia el formulario con los datos del departamento
      context['form'] = form
      return render(request, 'departamento/create.html', context)
   else:
      form = DepartamentoForm(request.POST,instance=departamento)
      if form.is_valid():
          form.save()
          return redirect('core:departamento_list')
      else:
          context['form'] = form
          return render(request, 'departamento/create.html', context)

@login_required
def departamento_delete(request, id):
    depto = get_object_or_404(Departamento, pk=id)
    if request.method == 'POST':
        depto.delete()
        return redirect('core:departamento_list')
    return render(request, 'delete/confirm_delete.html', {
        'object': depto,
        'object_name': 'departamento',
        'cancel_url': reverse('core:departamento_list')
    })

@login_required
## Vista para la lista de Tipos de Contrato
def tipoContrato_list(request):
    query = request.GET.get('q', None)
    if query:
        tipoContratos_list = TipoContrato.objects.filter(descripcion__icontains=query)
    else:
        tipoContratos_list = TipoContrato.objects.all().order_by('id')
    
    paginator = Paginator(tipoContratos_list, 5)
    page_number = request.GET.get('page')
    tipoContratos = paginator.get_page(page_number)
    
    context = {
        'tipoContratos': tipoContratos,
        'title': 'Listado de Tipos de Contrato',
        'query': query
    }
    return render(request, 'tipoContrato/list.html', context)


@login_required
def tipoContrato_create(request):
    context={'title':'Ingresar Tipo de Contrato'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")

        form = TipoContratoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'tipoContrato/create.html', context)
    else:
        #  print("entro por post")
        form = TipoContratoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # cargo = form.save(commit=False)# lo tiene en memoria
            # cargo.user = request.user
            # cargo.save() # lo guarda en la BD
            return redirect('core:tipoContrato_list')
        else:
            context['form'] = form
            return render(request, 'tipoContrato/create.html',context)

@login_required
def tipoContrato_update(request,id):
   context={'title':'Actualizar Tipo de Contrato'}
   tipoContrato = TipoContrato.objects.get(pk=id)
   if request.method == "GET":
      form = TipoContratoForm(instance=tipoContrato)# instancia el formulario con los datos del tipo de contrato
      context['form'] = form
      return render(request, 'tipoContrato/create.html', context)
   else:
      form = TipoContratoForm(request.POST,instance=tipoContrato)
      if form.is_valid():
          form.save()
          return redirect('core:tipoContrato_list')
      else:
          context['form'] = form
          return render(request, 'tipoContrato/create.html', context)


@login_required
def tipoContrato_delete(request, id):
    contrato = get_object_or_404(TipoContrato, pk=id)
    if request.method == 'POST':
        contrato.delete()
        return redirect('core:tipoContrato_list')
    return render(request, 'delete/confirm_delete.html', {
        'object': contrato,
        'object_name': 'tipo de contrato',
        'cancel_url': reverse('core:tipoContrato_list')
    })

@login_required
## Vista para la lista de empleados
def empleado_list(request):
    query_nombre = request.GET.get('nombre', None)
    query_cedula = request.GET.get('cedula', None)
    query_cargo = request.GET.get('cargo', None)
    
    empleados_list = Empleado.objects.all().order_by('id')
    
    # Aplicar filtros si existen
    if query_nombre:
        empleados_list = empleados_list.filter(nombre__icontains=query_nombre)
    if query_cedula:
        empleados_list = empleados_list.filter(cedula__icontains=query_cedula)
    if query_cargo:
        empleados_list = empleados_list.filter(cargo__descripcion__icontains=query_cargo)
    
    # Paginación
    paginator = Paginator(empleados_list, 10)
    page_number = request.GET.get('page')
    empleados = paginator.get_page(page_number)
    
    context = {
        'empleados': empleados,
        'title': 'Listado de empleados',
        'query_nombre': query_nombre,
        'query_cedula': query_cedula,
        'query_cargo': query_cargo,
        'cargos': Cargo.objects.all(), # Para el dropdown de cargos
        'departamentos': Departamento.objects.all() # Para el dropdown de departamentos
    }
    return render(request, 'empleado/list.html', context)


@login_required
def empleado_create(request):
    context={'title':'Ingresar Empleado'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")

        form = EmpleadoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'empleado/create.html', context)
    else:
        #  print("entro por post")
        form = EmpleadoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # cargo = form.save(commit=False)# lo tiene en memoria
            # cargo.user = request.user
            # cargo.save() # lo guarda en la BD
            return redirect('core:empleado_list')
        else:
            context['form'] = form
            return render(request, 'empleado/create.html',context)

@login_required
def empleado_update(request,id):
   context={'title':'Actualizar Empleado'}
   empleado = Empleado.objects.get(pk=id)
   if request.method == "GET":
      form = EmpleadoForm(instance=empleado)# instancia el formulario con los datos del empleado
      context['form'] = form
      return render(request, 'empleado/create.html', context)
   else:
      form = EmpleadoForm(request.POST,instance=empleado)
      if form.is_valid():
          form.save()
          return redirect('core:empleado_list')
      else:
          context['form'] = form
          return render(request, 'empleado/create.html', context)

@login_required
def empleado_delete(request, id):
    emp = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('core:empleado_list')
    return render(request, 'delete/confirm_delete.html', {
        'object': emp,
        'object_name': 'empleado',
        'cancel_url': reverse('core:empleado_list')
    })


@login_required
## Vista para la lista de roles
def rol_list(request):
    query_empleado = request.GET.get('empleado', '')
    query_aniomes = request.GET.get('aniomes', '')
    query_neto_min = request.GET.get('neto_min', '')
    query_neto_max = request.GET.get('neto_max', '')
    
    # Obtener todos los roles inicialmente
    roles_list = Rol.objects.all().order_by('-aniomes', 'empleado__nombres')
    
    # Aplicar filtros
    if query_empleado:
        roles_list = roles_list.filter(empleado__nombres__icontains=query_empleado)
    if query_aniomes:
        roles_list = roles_list.filter(aniomes__contains=query_aniomes)
    if query_neto_min:
        roles_list = roles_list.filter(neto__gte=float(query_neto_min))
    if query_neto_max:
        roles_list = roles_list.filter(neto__lte=float(query_neto_max))
    
    # Paginación
    paginator = Paginator(roles_list, 10)
    page_number = request.GET.get('page')
    roles = paginator.get_page(page_number)
    
    context = {
        'roles': roles,
        'title': 'Listado de roles de pago',
        'query_empleado': query_empleado,
        'query_aniomes': query_aniomes,
        'query_neto_min': query_neto_min,
        'query_neto_max': query_neto_max,
        'empleados': Empleado.objects.all().order_by('nombres')  # Para autocompletar
    }
    return render(request, 'rol/list.html', context)


@login_required
def rol_create(request):
    context = {'title': 'Ingresar Rol'}
    print("metodo: ", request.method)
    if request.method == "GET":
        form = RolForm()  # instancia el formulario con los campos vacios
        empleados = Empleado.objects.all()  # obtener todos los empleados
        context['form'] = form
        context['empleados'] = empleados  # agregar empleados al contexto
        return render(request, 'rol/create.html', context)
    else:
        form = RolForm(request.POST)  # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:rol_list')
        else:
            empleados = Empleado.objects.all()  # obtener todos los empleados en caso de error
            context['form'] = form
            context['empleados'] = empleados  # agregar empleados al contexto
            return render(request, 'rol/create.html', context)

@login_required
def rol_update(request,id):
   context={'title':'Actualizar Rol'}
   from django.shortcuts import get_object_or_404
   rol = get_object_or_404(Rol, pk=id)
   if request.method == "GET":
      form = RolForm(instance=rol)# instancia el formulario con los datos del rol
      context['form'] = form
      return render(request, 'rol/create.html', context)
   else:
      form = RolForm(request.POST,instance=rol)
      if form.is_valid():
          form.save()
          return redirect('core:rol_list')
      else:
          context['form'] = form
          return render(request, 'rol/create.html', context)

@login_required
def rol_delete(request, id):
    rol = get_object_or_404(Rol, pk=id)
    if request.method == "POST":
        rol.delete()
        return redirect('core:rol_list')
    return render(request, 'delete/confirm_delete.html', {
        'object': rol,
        'object_name': 'rol',
        'cancel_url': reverse('core:rol_list')
    })





