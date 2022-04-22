import random

from django.contrib.auth.models import User, Group
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils.crypto import get_random_string

from ControlDeAcceso.views.mail import enviar_correo
from ControlDeAcceso.views.mid_auth import AuthAbsView
from Empresa.models import Empresa
from Usuarios.models import Usuario, TokenCorreo


class UsuariosView(AuthAbsView):
    def get(self, request):
        if request.user.is_superuser:
            usuarios = Usuario.objects.all().exclude(usuario__is_superuser=True,
                                                     usuario__groups__in=[Group.objects.get(name='Usuario de Empresa')])
        else:
            usuarios = Usuario.objects.filter(empresa_id=request.session['empresa_id'])\
                .exclude(usuario_id=request.user.id)
        return render(request, 'Usuarios/index.html', {'usuarios': usuarios})


class UsuarioCrearView(AuthAbsView):
    def get(self, request):
        return render(request, 'Usuarios/modal_crear_editar.html', datos_render())

    @transaction.atomic
    def post(self, request):
        rq = request.POST
        usuario = Usuario.data_form_usuario(request.POST)
        username = rq.get('nombre', '').split(' ')[0] + '.' + rq.get('apellido', '').split(' ')[0]
        user = User.objects.create_user(
            first_name=rq.get('nombre', ''),
            last_name=rq.get('apellido', ''),
            email=rq.get('correo', ''),
            username=username.lower()
        )
        usuario.usuario = user
        if request.user.is_superuser:
            user.groups.add(Group.objects.get(name='Administrador de Empresa'))
        else:
            usuario.empresa_id = request.session['empresa_id']
            user.groups.add(Group.objects.get(name='Usuario de Empresa'))
        usuario.save()
        return redirect(reverse('usuarios:index'))


class UsuarioEditarView(AuthAbsView):
    def get(self, request, id):
        return render(request, 'Usuarios/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        rq = request.POST
        usuario = Usuario.data_form_usuario(request.POST)
        User.objects.filter(id=id).update(first_name=rq.get('nombre', ''), last_name=rq.get('apellido', ''),
                                          email=rq.get('correo', ''))
        usuario.id = Usuario.objects.get(usuario_id=id).id
        usuario.save(update_fields=['empresa_id', 'direccion', 'pais', 'departamento', 'ciudad'])
        return redirect(reverse('usuarios:index'))


class UsuarioInvitarView(AuthAbsView):
    def get(self, request):
        return render(request, 'Usuarios/modal_invitar_usuario.html')

    @transaction.atomic
    def post(self, request):
        token = get_random_string(length=30)
        correo = request.POST.get('correo', '')
        TokenCorreo.objects.create(token=token, ruta='', datos=request.session['empresa_id'])

        enviar_correo({'asunto': 'Invitación a CAD', 'lista_destinatarios': [correo]})
        return redirect(reverse('usuarios:index'))


class UsuarioEliminarView(AuthAbsView):
    @transaction.atomic
    def post(self, request, id):
        try:
            Usuario.objects.get(usuario_id=id).delete()
            User.objects.get(id=id).delete()
            return JsonResponse({"estado": "OK"})
        except:
            return JsonResponse({"estado": "error",
                                 "mensaje": 'No es posible realizar esta accion'})


def datos_render(id_usuario=None):
    empresas = [{'id': e.id, 'nombre': e.nombre_empresa} for e in Empresa.objects.all()]
    roles = Group.objects.values('id', 'name')
    datos = {'roles': roles, 'origen': 'CREAR', 'empresas': empresas}
    if id_usuario:
        datos['usuario'] = Usuario.objects.get(usuario_id=id_usuario)
        datos['origen'] = 'EDITAR'
    return datos
