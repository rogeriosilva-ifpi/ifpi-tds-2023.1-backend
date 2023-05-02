from fastapi import APIRouter, Depends, HTTPException, status

# from app.persistence.db_utils import obter_repository
from app.persistence.filme_mongodb_repository import FilmeMongoDBRepository
# from app.persistence.filme_repository import FilmeInMemoryRepository
from app.persistence.filme_pgdb_repository import FilmePostgreSQLRepository

from ..auth_utils import obter_usuario_logado
from ..viewmodels import Filme, UsuarioSimples

print('Filme Controller ✅')
routes = APIRouter()
prefix = '/filmes'

# Banco de Dados
# filme_repository = FilmeInMemoryRepository()
# filme_repository = FilmeMongoDBRepository()
filme_repository = FilmePostgreSQLRepository()
# filme_repository = Depends(obter_repository('filme'))


@routes.get('/')
def todos_filmes(
        skip: int | None = 0,
        take: int | None = 0,
        usuario: UsuarioSimples = Depends(obter_usuario_logado)
):
    filmes = filme_repository.todos(skip, take)
    filmes_usuario = list(
        filter(lambda filme: filme.usuario_id == usuario.id, filmes))
    return filmes_usuario


@routes.get('/{filme_id}')
def obter_filme(filme_id: int | str, usuario: UsuarioSimples = Depends(obter_usuario_logado)):
    filme = filme_repository.obter_um(filme_id)

    # fail fast
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não há filme com id = {filme_id }')

    if filme.usuario_id != usuario.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado!")

    return filme


@routes.post('/', status_code=status.HTTP_201_CREATED)
def novo_filme(filme: Filme,
               usuario: UsuarioSimples = Depends(obter_usuario_logado)
               ):
    filme.usuario_id = usuario.id
    return filme_repository.salvar(filme)


@routes.delete("/{filme_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def remover_filme(filme_id: int | str, usuario: UsuarioSimples = Depends(obter_usuario_logado)):
    filme = filme_repository.obter_um(filme_id)

    if not filme:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado!")

    if filme.usuario_id != usuario.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado!")

    filme_repository.remover(filme_id)


@routes.put('/{filme_id}')
def atualizar_filme(filme_id: int | str, filme: Filme, usuario: UsuarioSimples = Depends(obter_usuario_logado)):
    filme_encontrado = filme_repository.obter_um(filme_id)

    if not filme_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado")

    if filme_encontrado.usuario_id != usuario.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado!")

    filme.usuario_id = usuario.id

    return filme_repository.atualizar(filme_id, filme)
