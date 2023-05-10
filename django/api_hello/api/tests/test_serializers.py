from django.test import TestCase

from api.models import Filme
from api.serializers import FilmeSerializer


class FilmeSerializerTest(TestCase):
    def test_serializer_valido(self):
        filme = Filme(nome='Meu Filme', genero='DRAMA', ano=2019, duracao=120)
        serializer = FilmeSerializer(filme)
        self.assertEqual(serializer.data, {
                         'id': None,
                         'nome': 'Meu Filme',
                         'genero': 'DRAMA',
                         'ano': 2019,
                         'duracao': 120})
