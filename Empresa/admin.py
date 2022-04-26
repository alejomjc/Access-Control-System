from django.contrib import admin

from Empresa.models import UsuarioPuntoAtencion


@admin.register(UsuarioPuntoAtencion)
class UsuarioPuntoAtencionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'punto_acceso')
    list_display_links = ('id', 'usuario', 'punto_acceso')
    search_fields = ('id', 'usuario', 'punto_acceso')
