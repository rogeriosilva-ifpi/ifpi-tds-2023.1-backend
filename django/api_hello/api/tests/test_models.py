from django.test import TestCase

from api.models import Filme


class FilmeModelTest(TestCase):

    def test_deve_criar_um_filme(self):
        filme = Filme.objects.create(
            nome='Meu Filme', genero='DRAMA', ano=2019, duracao=120)
        self.assertEqual(filme.nome, 'Meu Filme')
        self.assertEqual(filme.genero, 'DRAMA')
