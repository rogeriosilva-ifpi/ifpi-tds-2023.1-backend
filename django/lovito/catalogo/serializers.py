from rest_framework import serializers

from catalogo.models import Categoria, ClasseProduto, Produto


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        # fields = ['id', 'nome']
        fields = '__all__'


class ClasseProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClasseProduto
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco']
