from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Remision  # Asegúrate de que Remision es el modelo correcto
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def home(request):
    return render(request,'home.html')
    

def consulta_estado(request):
    if request.method == 'POST':
        numero_estado = request.POST.get('numero_estado')
        
        try:
            # Realizar la consulta en el modelo Remision
            remision = Remision.objects.get(pk=numero_estado)
            contexto = {'remision':remision}
        except Remision.DoesNotExist:
            contexto = {'error': 'No se encontró ninguna remisión con ese número de estado.'}

        return render(request, 'consulta_estado.html', contexto)
    
    return render(request, 'consulta_estado.html')

def enviar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        email = request.POST.get('email').strip()
        mensaje = request.POST.get('mensaje').strip()

        # Validar correo electrónico
        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse("El correo electrónico no es válido", status=400)

        # Configura el correo que se enviará
        asunto = f"Nuevo mensaje de {nombre}"
        mensaje_correo = f"Nombre: {nombre}\nCorreo: {email}\nMensaje:\n{mensaje}"
        remitente = email  # El remitente es la persona que envió el mensaje

        try:
            send_mail(
                asunto,
                mensaje_correo,
                remitente,  # De quién es el mensaje
                [settings.EMAIL_RECIPIENT],  # A quién se enviará el mensaje (configurado en settings.py)
                fail_silently=False,
            )
            return redirect('/')  # Redirigir a una página de agradecimiento después de enviar el mensaje
        except Exception as e:
            return HttpResponse(f"Error al enviar el mensaje: {e}", status=500)

    return render(request, 'home.html')  # La página de contacto