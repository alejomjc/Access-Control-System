from django.urls import path

from Empresa.views import views

app_name = 'Empresa'


urlpatterns = [
    path('index', views.EmpresasView.as_view(), name='index'),
    path('crear', views.EmpresaCrearView.as_view(), name='crear'),
    path('editar/<int:id>', views.EmpresaEditarView.as_view(), name='editar'),
    path('eliminar/<int:id>', views.EmpresaEliminarView.as_view(), name='eliminar'),
]
