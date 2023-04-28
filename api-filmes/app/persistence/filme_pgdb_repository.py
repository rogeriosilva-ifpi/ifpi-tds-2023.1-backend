from sqlmodel import Session, select

from app.persistence.db_utils import obter_engine
from app.presentation.viewmodels import Filme


class FilmePostgreSQLRepository():

    def __init__(self):
        engine = obter_engine()
        self.session = Session(engine)

    def todos(self, skip, take):
        query = select(Filme)
        result = self.session.exec(query)
        return result.all()

    def salvar(self, filme: Filme):
        self.session.add(filme)
        self.session.commit()
        self.session.refresh(filme)
        self.session.close()
        return filme

    def obter_um(self, filme_id: int):
        query = select(Filme).where(Filme.id == filme_id)
        return self.session.exec(query).one_or_none()

    def remover(self, filme_id):
        filme = self.obter_um(filme_id)
        self.session.delete(filme)
        self.session.commit()
        self.session.close()

    def atualizar(self, filme_id, filme):
        pass
