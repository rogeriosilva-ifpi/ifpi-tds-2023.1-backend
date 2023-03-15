from pydantic import BaseModel


class Filme(BaseModel):
    id: int | None
    nome: str
    genero: str
    ano: int
    duracao: int
