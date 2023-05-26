from rest_framework import serializers

from catalogo.models import Categoria, ClasseProduto


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nome']


class ClasseProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClasseProduto
        fields = '__all__'
