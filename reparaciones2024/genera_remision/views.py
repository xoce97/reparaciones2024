from django.db import models
from django.shortcuts import render
from .models import Remision  # Asegúrate de que Remision es el modelo correcto

def home(request):
    return render(request,'home.html')
    
def consulta_estado(request):
    if request.method == 'POST':
        numero_estado = request.POST.get('numero_estado').strip()
        
        try:
            # Realizar la consulta en el modelo Remision
            remision = Remision.objects.get(pk=numero_estado)
            contexto = {'remision':remision}
        except Remision.DoesNotExist:
            contexto = {'error': 'No se encontró ninguna remisión con ese número de estado.'}

        return render(request, 'consulta_estado.html', contexto)
    
    return render(request, 'consulta_estado.html')

