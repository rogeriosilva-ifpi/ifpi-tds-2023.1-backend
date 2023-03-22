from bson.objectid import ObjectId
from pydantic import BaseModel


class Filme(BaseModel):
    id: int | None | str
    nome: str
    genero: str
    ano: int
    duracao: int

    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, filme):
        filme_ = Filme(id=str(filme['_id']),
                       nome=filme['nome'],
                       genero=filme['genero'],
                       duracao=filme['duracao'],
                       ano=filme['ano'])
        return filme_

    def toDict(self):
        return {
            "nome": self.nome,
            "genero": self.genero,
            "duracao": self.duracao,
            "ano": self.ano
        }


class User(BaseModel):
    id: int | None
    nome: str
    email: str
    senha: str
