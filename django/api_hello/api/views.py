from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Filme
from api.serializers import FilmeSerializer, UserSerializer


class HelloView(APIView):
    def get(self, request):
        return Response({'message': 'Hello Django + DRF'})


class ListCreateFilme(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # print(f'User: {request.user}')
        # serializer = FilmeSerializer(Filme.objects.all(), many=True)
        filmes = Filme.objects.filter(usuario=request.user)
        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteFilme(APIView):

    permission_classes = [IsAuthenticated]

    def get_filme(self, pk, usuario):
        try:
            return Filme.objects.get(pk=pk, usuario=usuario)
        except Filme.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        filme = self.get_filme(pk, request.user)
        serializer = FilmeSerializer(filme)
        return Response(serializer.data)

    def put(self, request, pk):
        filme = self.get_filme(pk, request.user)
        serializer = FilmeSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        filme = self.get_filme(pk, request.user)
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
