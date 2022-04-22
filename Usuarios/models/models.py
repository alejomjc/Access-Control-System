from django.contrib.auth.models import User
from django.db import models

from Empresa.models.models import Empresa


class Usuario(models.Model):
    usuario = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.DO_NOTHING, blank=False,
                                   null=False)
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.DO_NOTHING, blank=True,
                                null=True)
    direccion = models.CharField(max_length=100, verbose_name='Dirección', blank=True, null=True)
    telefono = models.BigIntegerField(verbose_name='Teléfono', blank=True, null=True)
    pais = models.CharField(max_length=50, verbose_name='Pais', blank=True, null=True)
    departamento = models.CharField(max_length=50, verbose_name='Departamento', blank=True, null=True)
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad', blank=True, null=True)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    @staticmethod
    def data_form_usuario(datos):
        usuario = Usuario()
        usuario.empresa_id = datos.get('empresa', None)
        usuario.direccion = datos.get('direccion', '')
        usuario.telefono = datos.get('telefono', '')
        usuario.pais = datos.get('pais', '')
        usuario.departamento = datos.get('departamento', '')
        usuario.ciudad = datos.get('ciudad', '')
        return usuario
