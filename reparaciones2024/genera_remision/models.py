from django.db import models

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_equipo = models.CharField(max_length=100)  # Ej: 'Laptop', 'Celular', etc.
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100, unique=True)
    descripcion_problema = models.TextField()
    
    def __str__(self):
        return self.tipo_equipo

class Remision(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)
    fecha_remision = models.DateField(auto_now_add=True)
    descripcion_trabajo = models.TextField()  # Detalles del trabajo realizado
    costo_reparacion = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=50,choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('completado', 'Completado')])
    fecha_entrega = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
   