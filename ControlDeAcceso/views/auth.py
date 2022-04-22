from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render, reverse
from django.views import View
from django.contrib import messages

from Usuarios.models import Usuario


class IniciarSesionView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        else:
            return render(request, 'Auth/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        else:
            username: str = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username.lower(), password=password)
            if user is not None:
                login(request, user)
                try:
                    usuario = Usuario.objects.get(usuario=user)
                    request.session['empresa_id'] = usuario.empresa_id
                except:
                    if not user.is_superuser:
                        logout(request)
                        return render(request, 'Auth/login.html')
            else:
                return render(request, 'Auth/login.html')


class CerrarSesion(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Se ha cerrado la sesión')
            return redirect(reverse('Administracion:inicio-sesion'))
        else:
            return redirect(reverse('Administracion:inicio-sesion'))