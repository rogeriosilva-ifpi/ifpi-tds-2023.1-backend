import bcrypt
from fastapi import APIRouter, HTTPException, status

from app.persistence.auth_mongodb_repository import AuthMongoDBRepository

from ..viewmodels import CriarUsuario

routes = APIRouter()
prefix = '/auth'

print('Auth Controller ✅')

auth_repository = AuthMongoDBRepository()


@routes.post('/signup', status_code=status.HTTP_201_CREATED)
def auth_signup(usuario: CriarUsuario):

    if usuario.senha != usuario.confirmacao_senha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Senhas não conferem!')

    usuario_usuario = auth_repository.obter_usuario_por_usuario(
        usuario.usuario)

    if usuario_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuário(login) já utilizado!')

    usuario_email = auth_repository.obter_usuario_por_email(usuario.email)

    if usuario_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email já cadastrado!')

    # Tudo OK
    usuario.senha = bcrypt.hashpw(str.encode(usuario.senha), bcrypt.gensalt())

    usuario_criado = auth_repository.criar_usuario(usuario)

    return usuario_criado


@routes.post('/signin')
def auth_signin():
    return 'Usuário logado'


@routes.get('/me')
def auth_me():
    return 'Me'
