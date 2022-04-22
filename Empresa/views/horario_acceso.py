from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from ControlDeAcceso.views.mid_auth import AuthAbsView
from Empresa.models.models import HorarioAcceso


class HorariosAccesosView(AuthAbsView):
    def get(self, request):
        horarios = HorarioAcceso.objects.filter(empresa_id=request.session["empresa_id"])
        return render(request, 'HorarioAcceso/index.html', {'horarios': horarios})


class HorarioAccesoCrearView(AuthAbsView):
    def get(self, request):
        return render(request, 'HorarioAcceso/modal_crear_editar.html', datos_render())

    @transaction.atomic
    def post(self, request):
        horario = HorarioAcceso.data_form_horario_acceso(request.POST)
        horario.empresa_id = request.session["empresa_id"]
        horario.save()
        return redirect(reverse('empresa:horario-acceso'))


class HorarioAccesoEditarView(AuthAbsView):
    def get(self, request, id):
        return render(request, 'HorarioAcceso/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        horario = HorarioAcceso.data_form_horario_acceso(request.POST)
        horario.id = id
        horario.save(update_fields=['hora_inicio', 'hora_finalizacion'])
        return redirect(reverse('empresa:horario-acceso'))


class HorarioAccesoEliminarView(AuthAbsView):
    @transaction.atomic
    def post(self, request, id):
        try:
            HorarioAcceso.objects.get(id=id).delete()
            return JsonResponse({"estado": "OK"})
        except:
            return JsonResponse({"estado": "error",
                                 "mensaje": 'No es posible realizar esta accion'})


def datos_render(id_horario=None):
    datos = {'origen': 'CREAR'}
    if id_horario:
        datos['horario'] = HorarioAcceso.objects.get(id=id_horario)
        datos['origen'] = 'EDITAR'
    return datos
