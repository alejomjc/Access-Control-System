from django.contrib.auth.models import User, Group
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from Usuarios.models import Usuario


class UsuariosView(View):
    def get(self, request):
        usuarios = Usuario.objects.all().exclude(usuario__is_superuser=True)
        return render(request, 'Usuarios/index.html', {'usuarios': usuarios})


class UsuarioCrearView(View):
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
            username=username
        )
        usuario.usuario = user
        rol = Group.objects.get(id=request.POST.get('rol')[0])
        user.groups.add(rol)
        usuario.save()

        return redirect(reverse('usuarios:index'))


class UsuarioEditarView(View):
    def get(self, request, id):
        return render(request, 'Usuarios/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        rq = request.POST
        usuario = Usuario.data_form_usuario(request.POST)
        user = User.objects.get(id=id)
        user.first_name = rq.get('nombre', ''),
        user.last_name = rq.get('apellido', ''),
        user.email = rq.get('correo', ''),
        user.save(update_fields=['first_name', 'last_name', 'email', ])

        usuario.usuario = user
        user.groups.remove()
        rol = Group.objects.get(id=request.POST.get('rol')[0])
        user.groups.add(rol)
        usuario.save(update_fields=['empresa_id', 'direccion', 'pais', 'departamento', 'ciudad'])
        return redirect(reverse('usuarios:index'))


class UsuarioEliminarView(View):
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
    roles = Group.objects.values('id', 'name')
    datos = {'roles': roles, 'origen': 'CREAR'}
    if id_usuario:
        datos['usuario'] = Usuario.objects.get(usuario_id=id_usuario)
        datos['origen'] = 'EDITAR'
    return datos
