from django.contrib import admin

from Empresa.models import UsuarioPuntoHorario


@admin.register(UsuarioPuntoHorario)
class UsuarioPuntoAtencionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'punto_horario')
    list_display_links = ('id', 'usuario', 'punto_horario')
    search_fields = ('id', 'usuario', 'punto_horario')
