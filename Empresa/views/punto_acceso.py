from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from ControlDeAcceso.views.mid_auth import AuthAbsView
from Empresa.models.models import HorarioAcceso, PuntoAcceso


class PuntosAccesosView(AuthAbsView):
    def get(self, request):
        # puntos = PuntoAcceso.objects.filter(empresa_id=request.session["empresa_id"])
        puntos = PuntoAcceso.objects.filter(empresa_id=2)
        return render(request, 'PuntoAcceso/index.html', {'puntos': puntos})


class PuntoAccesoCrearView(AuthAbsView):
    def get(self, request):
        return render(request, 'PuntoAcceso/modal_crear_editar.html', datos_render())

    @transaction.atomic
    def post(self, request):
        punto = PuntoAcceso.data_form_punto_acceso(request.POST)
        # punto.empresa_id = request.session["empresa_id"]
        punto.empresa_id = 2
        punto.save()
        for hor in request.POST.get('horario[]', []):
            punto.horario_acceso.add(HorarioAcceso.objects.get(id=hor))
        return redirect(reverse('empresa:punto-acceso'))


class PuntoAccesoEditarView(AuthAbsView):
    def get(self, request, id):
        return render(request, 'PuntoAcceso/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        punto = PuntoAcceso.data_form_punto_acceso(request.POST)
        punto.id = id
        punto.save(update_fields=['nombre', 'direccion', 'correo_electronico', 'longitud', 'latitud', 'estado'])
        punto.horario_acceso.remove()
        for hor in request.POST.get('horario[]', []):
            punto.horario_acceso.add(HorarioAcceso.objects.get(id=hor))
        return redirect(reverse('empresa:punto-acceso'))


class PuntoAccesoEliminarView(AuthAbsView):
    @transaction.atomic
    def post(self, request, id):
        try:
            PuntoAcceso.objects.get(id=id).delete()
            return JsonResponse({"estado": "OK"})
        except:
            return JsonResponse({"estado": "error",
                                 "mensaje": 'No es posible realizar esta accion'})


def datos_render(id_punto=None):
    estados = [{'id': True, 'nombre': 'Activo'}, {'id': False, 'nombre': 'Inactivo'}]
    # horarios = HorarioAcceso.objects.filter(empresa_id=request.session["empresa_id"])
    horarios = [{'id': hor.id, 'nombre': '{0}-{1}'.format(hor.hora_inicio, hor.hora_finalizacion)}
                for hor in HorarioAcceso.objects.filter(empresa_id=2)]
    datos = {'origen': 'CREAR', 'estados': estados, 'horarios': horarios}
    if id_punto:
        punto = PuntoAcceso.objects.get(id=id_punto)
        datos['punto'] = punto
        datos['valores_horarios'] = [ha.id for ha in punto.horario_acceso.all()]
        datos['origen'] = 'EDITAR'
    return datos
