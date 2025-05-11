from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from core.models import Cargo, Departamento , TipoContrato
from core.forms import CargoForm, DepartamentoForm, TipoContratoForm

def home(request):
    data = {
        'title': 'App Nominas',
        'description': 'Nominas de empleados',
        'author': 'Erick Pazmiño-Maykel Aroca',
        'year': 2025,
    }
    
    
    return render(request, 'home.html', data)


## Vista para la lista de cargos
def cargo_list(request):
    query = request.GET.get('q', None)
    print(query)  # Solo para debug
    if query:
        cargos = Cargo.objects.filter(descripcion__icontains=query)
    else:
        cargos = Cargo.objects.all()
    context = {'cargos': cargos, 'title': 'Listado de cargos'}
    return render(request, 'cargo/list.html', context)



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

def cargo_delete(request,id):
    cargo = Cargo.objects.get(pk=id)
    cargo.delete()
    return redirect('core:cargo_list')


## Vista para la lista de departamentos
def departamento_list(request):
    query = request.GET.get('q', None)
    print(query)  # Solo para debug
    if query:
        departamentos = Departamento.objects.filter(descripcion__icontains=query)
    else:
        departamentos = Departamento.objects.all()
    context = {'departamentos': departamentos, 'title': 'Listado de departamentos'}
    return render(request, 'departamento/list.html', context)



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

def departamento_delete(request,id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect('core:departamento_list')


## Vista para la lista de Tipos de Contrato
def tipoContrato_list(request):
    query = request.GET.get('q', None)
    print(query)  # Solo para debug
    if query:
        tipoContratos = TipoContrato.objects.filter(descripcion__icontains=query)
    else:
        tipoContratos = TipoContrato.objects.all()
    context = {'tipoContratos': tipoContratos, 'title': 'Listado de Tipos de Contrato'}
    return render(request, 'tipoContrato/list.html', context)



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

def tipoContrato_delete(request,id):
    tipoContrato = TipoContrato.objects.get(pk=id)
    tipoContrato.delete()
    return redirect('core:tipoContrato_list')





