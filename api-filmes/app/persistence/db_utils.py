from decouple import config
from sqlmodel import SQLModel, create_engine


def get_engine():
    database_url = config('POSTGRESQL_URL')

    engine = create_engine(database_url, echo=True)
    SQLModel.metadata.create_all(engine)
    return engine
