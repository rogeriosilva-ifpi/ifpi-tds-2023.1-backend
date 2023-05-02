from typing import Literal

from decouple import config
from sqlmodel import create_engine

# from app.persistence.auth_mongodb_repository import AuthMongoDBRepository
# from app.persistence.filme_pgdb_repository import FilmePostgreSQLRepository


def obter_engine():
    return create_engine(config('POSTGRESQL_URL'), echo=True)


# def obter_repository(nome: Literal['filme', 'auth']):
#     if nome == 'filme':
#         return FilmePostgreSQLRepository()
#     elif nome == 'auth':
#         return AuthMongoDBRepository()
