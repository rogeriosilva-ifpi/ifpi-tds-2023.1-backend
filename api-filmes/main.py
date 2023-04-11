from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.presentation.controllers import auth_controller, filme_controller
from app.presentation.log_middleware import LogMiddleware

app = FastAPI()

origins = ['http://localhost:5500',
           'http://127.0.0.1:5500',
           'https://ifpi-tds-2023-1-backend.pages.dev']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

app.add_middleware(LogMiddleware)

# Rotas e Controllers
app.include_router(filme_controller.routes,
                   prefix=filme_controller.prefix)
app.include_router(auth_controller.routes,
                   prefix=auth_controller.prefix)
