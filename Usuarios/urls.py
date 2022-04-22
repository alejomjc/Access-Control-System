from django.urls import path

from Usuarios.views import views, token

app_name = 'Usuarios'


urlpatterns = [
    path('index', views.UsuariosView.as_view(), name='index'),
    path('crear', views.UsuarioCrearView.as_view(), name='crear'),
    path('invitar', views.UsuarioInvitarView.as_view(), name='invitar'),
    path('editar/<int:id>', views.UsuarioEditarView.as_view(), name='editar'),
    path('eliminar/<int:id>', views.UsuarioEliminarView.as_view(), name='eliminar'),
    path('token/<str:token>', token.TokenCorreoView.as_view(), name='token'),
]
