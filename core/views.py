from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from core.models import Cargo
from core.forms import CargoForm
def home(request):
    data = {
        'title': 'App Nominas',
        'description': 'Nominas de empleados',
        'author': 'Erick Pazmiño-Maykel Aroca',
        'year': 2025,
    }
    
    return render(request, 'home.html', data)

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