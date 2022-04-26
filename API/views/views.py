import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from API.serializers.serializers import PuntoAccesoSerializer
from Empresa.models import UsuarioPuntoHorario, PuntoAcceso


class UsuarioHorarioPuntoAccesoViewSet(ViewSet):
    def list(self, request):
        hora = datetime.datetime.now().time()
        upa = UsuarioPuntoHorario.objects\
            .filter(usuario__username=request.GET.get('username'),
                    punto_horario__horario_acceso__empresa__nombre_empresa=request.GET.get('empresa'),
                    punto_horario__punto_acceso__nombre=request.GET.get('sede'))
        acceso = False
        for hr in upa:
            if hora > hr.punto_horario.horario_acceso.hora_inicio and \
                    hora < hr.punto_horario.horario_acceso.hora_finalizacion:
                acceso = True
                break
        if acceso:
            pa = PuntoAcceso.objects.filter(id=upa.first().punto_horario.punto_acceso_id)
            serializer = PuntoAccesoSerializer(pa, many=True)
            return Response({'resultado': 'True', 'sede': serializer.data})
        else:
            return Response('False', status=status.HTTP_400_BAD_REQUEST)
