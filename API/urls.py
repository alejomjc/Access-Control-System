from django.urls import path

from API.views.views import UsuarioHorarioPuntoAccesoViewSet

app_name = 'API'


urlpatterns = [
    path('consultar-acceso', UsuarioHorarioPuntoAccesoViewSet.as_view({'get': 'list'}), name='consultar-acceso'),
]