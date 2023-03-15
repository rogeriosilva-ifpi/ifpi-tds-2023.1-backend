from pydantic import BaseModel


class Filme(BaseModel):
    id: int | None
    nome: str
    genero: str
    ano: int
    duracao: int


class User(BaseModel):
    id: int | None
    nome: str
    email: str
    senha: str
