from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import registry
from sqlmodel import Field, SQLModel

mapper_registry = registry()


class Filme(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    nome: str
    genero: str
    ano: int
    duracao: int
    usuario_id: int | None = Field(foreign_key='usuario.id', default=None)


class Usuario(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr
    senha: str = Field(min_length=6)


class UsuarioSimples(Usuario):
    pass


class CriarUsuario(BaseModel):
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr
    senha: str = Field(min_length=6)
    confirmacao_senha: str


class LoginData(BaseModel):
    usuario: str = Field(min_length=5)
    senha: str = Field(min_length=6)
