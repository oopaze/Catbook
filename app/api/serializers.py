from rest_framework import serializers
from tabelas.models import Publicacao

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ['text', 'user', 'image']