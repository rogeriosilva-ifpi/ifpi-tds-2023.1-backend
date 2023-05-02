from bson.objectid import ObjectId
from decouple import config
from pymongo import MongoClient
from sqlmodel import Session, select

from app.persistence.db_utils import obter_engine

from ..presentation.viewmodels import Usuario


class AuthPostgreSQLRepository():

    def __init__(self):
        self.session = Session(obter_engine())

    def criar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        self.session.close()
        return usuario

    def obter_usuario_por_id(self, id: int):
        query = select(Usuario).where(Usuario.id == id)
        return self.session.exec(query).one_or_none()

    def obter_usuario_por_email(self, email: str):
        query = select(Usuario).where(Usuario.email == email)
        return self.session.exec(query).one_or_none()

    def obter_usuario_por_usuario(self, usuario: str):
        query = select(Usuario).where(Usuario.usuario == usuario)
        return self.session.exec(query).one_or_none()
