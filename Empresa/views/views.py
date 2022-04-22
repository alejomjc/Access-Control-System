from django.contrib.auth.models import User
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from Empresa.models.models import Empresa


class EmpresasView(View):
    def get(self, request):
        empresas = Empresa.objects.all()
        return render(request, 'Empresa/index.html', {'empresas': empresas})


class EmpresaCrearView(View):
    def get(self, request):
        return render(request, 'Empresa/modal_crear_editar.html', datos_render())

    @transaction.atomic
    def post(self, request):
        empresa = Empresa.data_form_empresa(request.POST)
        empresa.save()
        return redirect(reverse('empresa:index'))


class EmpresaEditarView(View):
    def get(self, request, id):
        return render(request, 'Empresa/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        empresa = Empresa.data_form_empresa(request.POST)
        empresa.id = id
        empresa.save(update_fields=['nit', 'nombre_empresa', 'nombre_comercial', 'direccion', 'telefono',
                                    'correo_electronico', 'url_web', 'pais', 'departamento', 'ciudad'])
        return redirect(reverse('empresa:index'))


class EmpresaEliminarView(View):
    @transaction.atomic
    def post(self, request, id):
        try:
            Empresa.objects.get(id=id).delete()
            return JsonResponse({"estado": "OK"})
        except:
            return JsonResponse({"estado": "error",
                                 "mensaje": 'No es posible realizar esta accion'})


def datos_render(id_empresa=None):
    usuarios = User.objects.exclude(is_superuser=True).values('id', 'first_name', 'last_name')
    datos = {'usuarios': usuarios, 'origen': 'CREAR'}
    if id_empresa:
        datos['empresa'] = Empresa.objects.get(id=id_empresa)
        datos['origen'] = 'EDITAR'
    return datos
