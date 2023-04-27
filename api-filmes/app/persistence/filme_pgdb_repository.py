from fastapi import Depends
from sqlmodel import Session, select

from app.persistence.db_utils import get_engine
from app.presentation.viewmodels import Filme


class FilmePostgreSQLDBRepository():

    def __init__(self):
        engine = get_engine()
        self.session = Session(engine)

    def todos(self, skip=0, take=0):
        query = select(Filme)
        filmes = self.session.exec(query).all()
        return filmes

    def salvar(self, filme):
        self.session.add(filme)
        self.session.commit()
        self.session.refresh(filme)
        return filme

    def obter_um(self, filme_id):
        pass

    def remover(self, filme_id):
        pass

    def atualizar(self, filme_id, filme):
        pass
