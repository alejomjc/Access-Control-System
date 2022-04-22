from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from Empresa.models import Empresa
from Usuarios.models import TokenCorreo


class TokenCorreoView(View):
    def get(self, request, token):
        tok = TokenCorreo.objects.get(token=token)
        if tok.activo:
            tok.activo = False
            tok.save(update_fields=['activo'])
            empresa = Empresa.objects.get(id=tok.datos)
            return render(request, 'Usuarios/register.html', {'empresa': empresa})
        else:
            return redirect(reverse('cerrar-sesion'))
