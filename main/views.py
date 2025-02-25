from django.shortcuts import render
from .models import Vehiculo

def inicio(request):
    #Página de inicio
    return render(request, 'main/inicio.html')

def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'main/vehiculos.html', {'vehiculos': vehiculos})

def empresa(request):
    #Página de empresa
    return render(request, 'main/empresa.html')

def servicios(request):
    #Página de servicios
    return render(request, 'main/servicios.html')


def contacto(request):
    #Página de contacto
    return render(request, 'main/contacto.html')