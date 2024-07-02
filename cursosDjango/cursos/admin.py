from django.contrib import admin
from .models import CursosAlmacenados
from .models import Actividad


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'email', 'curso', 'modulos', 'precio', 'comentario')
    search_fields = ('nombre', 'email', 'curso', 'modulos', 'precio', 'comentario')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'email')


admin.site.register(CursosAlmacenados, AdministrarModelo)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ('claveActividad', 'descripcion')
    search_fields = ('claveActividad', 'descripcion')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'claveActividad')

admin.site.register(Actividad, AdministrarActividades)
