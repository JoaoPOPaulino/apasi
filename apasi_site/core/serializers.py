from rest_framework import serializers
from .models import Cidade, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla']

class CidadeSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='estado.sigla')
    class Meta:
        model = Cidade
        fields = ['nome', 'state', 'is_sede', 'lat', 'lng']