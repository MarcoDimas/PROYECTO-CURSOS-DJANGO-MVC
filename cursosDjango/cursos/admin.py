from django.contrib import admin
from .models import CursosAlmacenados

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'email', 'curso', 'modulos', 'precio', 'comentario')
    search_fields = ('nombre', 'email', 'curso', 'modulos', 'precio', 'comentario')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'email')


admin.site.register(CursosAlmacenados, AdministrarModelo)