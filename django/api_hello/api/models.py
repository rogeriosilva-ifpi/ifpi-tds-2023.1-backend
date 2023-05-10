from django.contrib.auth import get_user_model
from django.db import models

GENERO_CHOICES = [
    ('C', 'COMÉDIA'),
    ('D', 'DRAMA'),
    ('A', 'AVENTURA'),
    ('T', 'TERROR')
]

User = get_user_model()


class Filme(models.Model):
    nome = models.CharField()
    genero = models.CharField(choices=GENERO_CHOICES)
    ano = models.PositiveIntegerField()
    duracao = models.PositiveIntegerField()
    usuario = models.ForeignKey(
        User, related_name='filmes', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome} - {self.ano}'
