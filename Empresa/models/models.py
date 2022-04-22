from django.contrib.auth.models import User
from django.db import models


class Empresa(models.Model):
    usuario_admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuario Admin',
                                      blank=True, null=True)
    nit = models.CharField(max_length=15, verbose_name='NIT', blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, verbose_name='Nombre de la Empresa', blank=True, null=True)
    nombre_comercial = models.CharField(max_length=100, verbose_name='Nombre Comercial', blank=True, null=True)
    direccion = models.CharField(max_length=50, verbose_name='Dirección', blank=True, null=True)
    telefono = models.CharField(max_length=50, verbose_name='Teléfono', blank=True, null=True)
    correo_electronico = models.EmailField(verbose_name='Correo Electrónico', blank=True, null=True)
    url_web = models.CharField(max_length=50, verbose_name='Url de la Web', blank=True, null=True)
    pais = models.CharField(max_length=50, verbose_name='Pais', blank=True, null=True)
    departamento = models.CharField(max_length=50, verbose_name='Departamento', blank=True, null=True)
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad', blank=True, null=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    @staticmethod
    def data_form_empresa(datos):
        empresa = Empresa()
        empresa.nit = datos.get('nit', None)
        empresa.nombre_empresa = datos.get('nombre_empresa', '')
        empresa.nombre_comercial = datos.get('nombre_comercial', '')
        empresa.direccion = datos.get('direccion', '')
        empresa.telefono = datos.get('telefono', '')
        empresa.correo_electronico = datos.get('correo_electronico', '')
        empresa.url_web = datos.get('url_web', '')
        empresa.pais = datos.get('pais', '')
        empresa.departamento = datos.get('departamento', '')
        empresa.ciudad = datos.get('ciudad', '')
        return empresa


class HorarioAcceso(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, blank=False, null=False)
    hora_inicio = models.TimeField(max_length=100, verbose_name='Nombre de la Empresa', blank=True, null=True)
    hora_finalizacion = models.TimeField(max_length=100, verbose_name='Nombre de la Empresa', blank=True, null=True)

    def __str__(self):
        return 'Franja: {0} - {1}'.format(self.hora_inicio, self.hora_finalizacion)

    class Meta:
        verbose_name = 'Horario de Acceso'
        verbose_name_plural = 'Horarios de Acceso'

    @staticmethod
    def data_form_horario_acceso(datos):
        horario = HorarioAcceso()
        horario.hora_inicio = datos.get('hora_inicio', '')
        horario.hora_finalizacion = datos.get('hora_finalizacion', '')
        return horario


class PuntoAcceso(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, verbose_name='Empresa', blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Empresa', blank=True, null=True)
    direccion = models.CharField(max_length=50, verbose_name='Dirección', blank=True, null=True)
    correo_electronico = models.EmailField(verbose_name='Correo Electrónico', blank=True, null=True)
    longitud = models.CharField(max_length=50, verbose_name='Pais', blank=True, null=True)
    latitud = models.CharField(max_length=50, verbose_name='Pais', blank=True, null=True)
    horario_acceso = models.ManyToManyField(HorarioAcceso, verbose_name='Horarios de Acceso', blank=True, null=True)
    estado = models.BooleanField(verbose_name='Url de la Web', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Punto de Acceso'
        verbose_name_plural = 'Puntos de Acceso'

    @staticmethod
    def data_form_punto_acceso(datos):
        punto = PuntoAcceso()
        punto.nombre = datos.get('nombre', '')
        punto.direccion = datos.get('direccion', '')
        punto.correo_electronico = datos.get('correo_electronico', '')
        punto.longitud = datos.get('longitud', '')
        punto.latitud = datos.get('latitud', '')
        punto.estado = datos.get('estado', '')
        return punto


class UsuarioPuntoAtencion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Empresa', blank=True, null=True)
    punto_acceso = models.ForeignKey(PuntoAcceso, on_delete=models.DO_NOTHING, verbose_name='Empresa', blank=True, null=True)

    def __str__(self):
        return '{0}-{1}'.format(self.usuario, self.punto_acceso)

    class Meta:
        verbose_name = 'Usuario Punto de Atención'
        verbose_name_plural = 'Usuarios Puntos de Atencion'







