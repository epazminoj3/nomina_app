from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.models import Cargo
####from core.forms import DoctorForm
def home(request):
    data = {
        'title': 'App Nominas',
        'description': 'Nominas de empleados',
        'author': 'Erick Pazmiño-Maykel Aroca',
        'year': 2025,
    }
    
    return render(request, 'home.html', data)

def cargo_list(request):

    query=request.GET.get('q',None)
    print(query)
    if query: cargos=Cargo.objects.filter(name__icontains=query)
    else: cargos=Cargo.objects.all()
    context={'cargos':cargos,'title':'listado de cargos'}
    return render(request,'cargo/list.html', context)

def cargo_create(request): 
    pass

def cargo_update(request,id):
    pass

def cargo_delete(request,id):
    pass