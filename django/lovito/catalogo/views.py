from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Categoria, ClasseProduto
from .serializers import CategoriaSerializer, ClasseProdutoSerializer


class ListCategoriaView(APIView):

    def get(self, request):

        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data)


class ListClasseProdutoView(ListAPIView):
    queryset = ClasseProduto.objects.all()
    serializer_class = ClasseProdutoSerializer
