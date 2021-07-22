from rest_framework import serializers

from website.models import Huesped, Cliente

class HuespedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Huesped
        fields = ['url', 'rut_huesped','dv','nombre','telefono','email']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'rut_cliente','dv','nombre','telefono','email']