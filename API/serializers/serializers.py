from rest_framework import serializers


class PuntoAccesoSerializer(serializers.Serializer):
    empresa = serializers.CharField()
    nombre = serializers.CharField()
    direccion = serializers.CharField()
    correo_electronico = serializers.EmailField()
    longitud = serializers.CharField()
    latitud = serializers.CharField()
