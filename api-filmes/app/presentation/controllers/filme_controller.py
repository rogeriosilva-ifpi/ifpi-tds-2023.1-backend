from fastapi import APIRouter, HTTPException, status

from ..viewmodels import Filme

routes = APIRouter()
prefix = '/filmes'


filmes: list[Filme] = []


@routes.get('/')
def todos_filmes(skip: int | None = None, take: int | None = None):
    inicio = skip

    if skip and take:
        fim = skip + take
    else:
        fim = None

    return filmes[inicio:fim]


@routes.get('/{filme_id}')
def obter_filme(filme_id: int):
    # print(f'Foi pedido o ID: {filme_id}')
    for filme in filmes:
        if filme.id == filme_id:
            return filme

    # Não encontrado
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return f'Não localizado filme com id={filme_id}'

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Não há filme com id = {filme_id }')


@routes.post('/', status_code=status.HTTP_201_CREATED)
def novo_filme(filme: Filme):
    filme.id = len(filmes) + 100
    filmes.append(filme)

    return filme


@routes.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_filme(filme_id: int):
    for filme_atual in filmes:
        if filme_atual.id == filme_id:
            filmes.remove(filme_atual)
            return

    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Filme não encontrado")


@routes.put('/{filme_id}')
def atualizar_filme(filme_id: int, filme: Filme):
    for index in range(len(filmes)):
        filme_atual = filmes[index]
        if filme_atual.id == filme_id:
            filme.id = filme_atual.id
            filmes[index] = filme
            return filme

    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Filme não encontrado")
