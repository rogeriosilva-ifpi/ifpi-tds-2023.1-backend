from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel


class Filme(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    genero: str
    ano: int
    duracao: int
    usuario_id: int | None = Field(default=None, foreign_key="usuario.id")

    @classmethod
    def fromDict(cls, filme_dict):
        filme_ = Filme(id=str(filme_dict['_id']),
                       nome=filme_dict['nome'],
                       genero=filme_dict['genero'],
                       duracao=filme_dict['duracao'],
                       ano=filme_dict['ano'],
                       usuario_id=str(filme_dict['usuario_id']))
        return filme_

    def toDict(self):
        return {
            "nome": self.nome,
            "genero": self.genero,
            "duracao": self.duracao,
            "ano": self.ano,
            "usuario_id": self.usuario_id
        }


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr
    senha: str = Field(min_length=6)


class CriarUsuario(Usuario):
    confirmacao_senha: str


class LoginData(BaseModel):
    usuario: str = Field(min_length=5)
    senha: str = Field(min_length=6)
