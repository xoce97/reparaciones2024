from django.shortcuts import render
from django.http import HttpResponse
from .models import Remision  # Asegúrate de que Remision es el modelo correcto

def consulta_estado(request):
    if request.method == 'POST':
        numero_estado = request.POST.get('numero_estado')
        
        try:
            # Realizar la consulta en el modelo Remision
            remision = Remision.objects.get(numero_remision=numero_estado)
            contexto = {'remision': remision}
        except Remision.DoesNotExist:
            contexto = {'error': 'No se encontró ninguna remisión con ese número de estado.'}

        return render(request, 'consulta_estado.html', contexto)
    
    return render(request, 'consulta_estado.html')
