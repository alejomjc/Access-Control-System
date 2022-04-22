"""ControlDeAcceso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ControlDeAcceso.views.view import IndexView
from ControlDeAcceso.views import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('iniciar-sesion', auth.IniciarSesionView.as_view(), name='iniciar-sesion'),
    path('cerrar-sesion', auth.CerrarSesion.as_view(), name='cerrar-sesion'),
    path('usuarios/', include('Usuarios.urls', namespace='usuarios')),
    path('empresa/', include('Empresa.urls', namespace='empresa')),
]
