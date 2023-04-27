from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.user_service import UsuarioService
from app.infrastructure.cryptograph.hash_provider import HashProvider
from app.infrastructure.cryptograph.jwt_token_provider import JWTTokenProvider
from app.persistence.auth_mongodb_repository import AuthMongoDBRepository

from ..auth_utils import obter_usuario_logado
from ..viewmodels import CriarUsuario, LoginData, Usuario

routes = APIRouter()
prefix = '/auth'

print('Auth Controller ✅')

# Dependencias
auth_repository = AuthMongoDBRepository()
hash_provider = HashProvider()
jwt_provider = JWTTokenProvider()


@routes.post('/signup2', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def auth_signup2(usuario: CriarUsuario, usuario_service: UsuarioService = Depends(UsuarioService)):
    return usuario_service.criar_usuario(usuario)


@routes.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
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
    usuario.senha = hash_provider.hash(usuario.senha)

    usuario_criado = auth_repository.criar_usuario(usuario)

    return usuario_criado


@routes.post('/signin')
def auth_signin(login_data: LoginData):
    usuario = auth_repository.obter_usuario_por_usuario(login_data.usuario)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuário e/ou senha incorreto(s)!')

    if hash_provider.verify(login_data.senha, usuario.senha):
        token = jwt_provider.sign({'usuario_id': usuario.id})
        return {'access_token': token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuário e/ou senha incorreto(s)!')


@routes.get('/me', response_model=Usuario)
async def auth_me(user: Usuario = Depends(obter_usuario_logado)):
    return user
