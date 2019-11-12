from django.shortcuts import render
from .models import  Programador, Proyecto
from django.utils import timezone


#muestra un inicio de la pagina
def inicio(request):   
    return render(request, 'post/index.html')



#muestra un listado de los programadores por orden alfabetico 
def programadores_list(request):
    listado = Programador.objects.all().order_by('correo')
    return render(request, 'post/programers.html', {'listado':listado})


#muestra un listado de los proyectos por fecha de creacion 
def proyectos_list(request):
    listado = Proyecto.objects.all().order_by('fecha_creacion')
    return render(request, 'post/proyectos.html', {'listado':listado})


#realiza una busqueda de un proyecto 
def proyecto_search(request):
    listado = Programador.objects.all().order_by('correo')
    return render(request, 'post/#', {'posts':posts})
# Create your views here.

def nosotros(request):   
    return render(request, 'post/nosotros.html')