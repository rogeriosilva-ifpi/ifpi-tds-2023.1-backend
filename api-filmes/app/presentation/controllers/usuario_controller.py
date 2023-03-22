from fastapi import APIRouter

routes = APIRouter()
prefix = '/usuarios'

print('Usuário Controller ✅')


@routes.get('/')
def todos_usuario():
    return []
