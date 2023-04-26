from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field


class Filme(BaseModel):
    id: int | None | str
    nome: str
    genero: str
    ano: int
    duracao: int
    usuario_id: int | str | None

    class Config:
        orm_mode = True

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


class UsuarioSimples(BaseModel):
    id: int | None | str
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr

    def toDict(self):
        return {
            "nome": self.nome,
            "usuario": self.usuario,
            "email": self.email,
            "senha": self.senha,
        }


class Usuario(UsuarioSimples):
    senha: str = Field(min_length=6)

    @classmethod
    def fromDict(cls, usuario_dict):
        return Usuario(**usuario_dict, id=str(usuario_dict['_id']))


class CriarUsuario(Usuario):
    confirmacao_senha: str


class LoginData(BaseModel):
    usuario: str = Field(min_length=5)
    senha: str = Field(min_length=6)
