from django.urls import path

from Usuarios.views import views

app_name = 'Usuarios'


urlpatterns = [
    path('index', views.UsuariosView.as_view(), name='index'),
    path('crear', views.UsuarioCrearView.as_view(), name='crear'),
    path('editar/<int:id>', views.UsuarioEditarView.as_view(), name='editar'),
    path('eliminar/<int:id>', views.UsuarioEliminarView.as_view(), name='eliminar'),
]
