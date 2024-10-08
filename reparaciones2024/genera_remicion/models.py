from django.db import models
import uuid

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Equipo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_equipo = models.CharField(max_length=100)  # Ej: 'Laptop', 'Celular', etc.
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100, unique=True)
    descripcion_problema = models.TextField()

    

class Remision(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_remision = models.DateField(auto_now_add=True)
    numero_remision = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    descripcion_trabajo = models.TextField()  # Detalles del trabajo realizado
    costo_reparacion = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(
        max_length=50,
        choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('completado', 'Completado')]
    )
    fecha_entrega = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

