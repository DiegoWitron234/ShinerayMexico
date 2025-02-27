from django.shortcuts import render, get_object_or_404
from .models import Vehiculo

def inicio(request):
    #Página de inicio
    return render(request, 'main/inicio.html')

def vehiculos(request):
    query = request.GET.get('q')
    if query:
        autos = Vehiculo.objects.filter(modelo__icontains=query)
    else:
        autos = Vehiculo.objects.all()
    return render(request, 'main/vehiculos.html', {'vehiculos': autos})

def vehiculo_detalles(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    context = {'vehiculo': vehiculo}
    return render(request, 'main/vehiculo_detalles.html', context)

def empresa(request):
    #Página de empresa
    return render(request, 'main/empresa.html')

def servicios(request):
    #Página de servicios
    return render(request, 'main/servicios.html')


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # Aquí podrías usar send_mail o guardar en la BD
        # send_mail(
        #     subject=f"Mensaje de {nombre}",
        #     message=mensaje,
        #     from_email=email,
        #     recipient_list=[settings.DEFAULT_FROM_EMAIL],
        # )
        return render(request, 'main/contacto.html', {'enviado': True})
    return render(request, 'main/contacto.html')