from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Filme
from .serializers import FilmeSerializer, UserSerializer


class ListCreateFilmeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        filmes = Filme.objects.filter(usuario=user)
        serializer = FilmeSerializer(filmes, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        usuario = request.user
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = usuario
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteFilmeView(APIView):

    permission_classes = [IsAuthenticated]

    def get_filme(self, usuario, pk):
        try:
            return Filme.objects.get(pk=pk, usuario=usuario)
        except Filme.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        filme = self.get_filme(request.user, pk)
        serializer = FilmeSerializer(filme)
        return Response(data=serializer.data)

    def put(self, request, pk):
        filme = self.get_filme(request.user, pk)
        serializer = FilmeSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        filme = self.get_filme(request.user, pk)
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):

    def get(self, request):
        data = {'message': 'Hello 366 --> Django + DRF!'}
        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        return Response({'message': f'POST: Ok! {nome}'})
