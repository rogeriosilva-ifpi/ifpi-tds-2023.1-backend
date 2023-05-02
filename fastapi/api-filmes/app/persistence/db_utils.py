from decouple import config
from sqlmodel import create_engine


def obter_engine():
    return create_engine(config('POSTGRESQL_URL'), echo=True)
