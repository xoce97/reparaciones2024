from django.contrib import admin
from .models import Cliente,Equipo,Tecnico,Remision

class RemisionAdmin(admin.ModelAdmin):
    list_display = ('numero_remision', 'descripcion_trabajo', 'costo_reparacion', 'estatus', 'fecha_remision')  # Campos a mostrar en la lista
    search_fields = ('numero_remision', 'descripcion_trabajo')  # Campos que se pueden buscar
    list_filter = ('estatus',)

admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Tecnico)
admin.site.register(Remision,RemisionAdmin)

# Register your models here.
