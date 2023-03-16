from fastapi import APIRouter

routes = APIRouter()
prefix = '/usuarios'


@routes.get('/')
def todos_usuario():
    return []
