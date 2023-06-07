from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Categoria, ClasseProduto
from .serializers import (CategoriaSerializer, ClasseProdutoSerializer,
                          ProdutoSerializer)
from .services import CategoriaService, ProdutoService

categoriaService = CategoriaService()
produtoService = ProdutoService()


class ListProdutoView(APIView):

    def get(self, request):
        produtos = produtoService.ativos()
        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data)


class ListCategoriaView(APIView):

    def get(self, request):

        categorias = categoriaService.obter_ordenado('nome', inverso=False)
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data)


class ListClasseProdutoView(ListAPIView):
    queryset = ClasseProduto.objects.all().order_by('nome')
    serializer_class = ClasseProdutoSerializer
