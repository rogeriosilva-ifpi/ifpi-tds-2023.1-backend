from fastapi import APIRouter, HTTPException, status

from app.persistence.filme_mongodb_repository import FilmeMongoDBRepository
from app.persistence.filme_repository import FilmeInMemoryRepository

from ..viewmodels import Filme

print('Filme Controller ✅')
routes = APIRouter()
prefix = '/filmes'

# Banco de Dados
# filme_repository = FilmeInMemoryRepository()
filme_repository = FilmeMongoDBRepository()


@routes.get('/')
def todos_filmes(skip: int | None = 0, take: int | None = 0):
    return filme_repository.todos(skip, take)


@routes.get('/{filme_id}')
def obter_filme(filme_id: int | str):
    filme = filme_repository.obter_um(filme_id)

    # fail fast
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não há filme com id = {filme_id }')

    return filme


@routes.post('/', status_code=status.HTTP_201_CREATED)
def novo_filme(filme: Filme):
    return filme_repository.salvar(filme)


@routes.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_filme(filme_id: int | str):
    filme = filme_repository.obter_um(filme_id)

    if not filme:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado")

    filme_repository.remover(filme_id)


@routes.put('/{filme_id}')
def atualizar_filme(filme_id: int | str, filme: Filme):
    filme_encontrado = filme_repository.obter_um(filme_id)

    if not filme_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado")

    return filme_repository.atualizar(filme_id, filme)
