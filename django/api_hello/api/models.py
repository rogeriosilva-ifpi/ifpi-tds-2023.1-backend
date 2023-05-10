from django.contrib.auth import get_user_model
from django.db import models
from pyexpat import model

GENERO_CHOICES = [
    ('DRAMA', 'DRAMA'),
    ('COMEDIA', 'COMÉDIA'),
    ('AVENTURA', 'AVENTURA'),
]

User = get_user_model()


class Filme(models.Model):
    nome = models.CharField()
    genero = models.CharField(choices=GENERO_CHOICES)
    ano = models.PositiveIntegerField()
    duracao = models.PositiveIntegerField()
    usuario = models.ForeignKey(
        User, related_name='filmes', on_delete=models.SET_NULL, null=True, default=None)
