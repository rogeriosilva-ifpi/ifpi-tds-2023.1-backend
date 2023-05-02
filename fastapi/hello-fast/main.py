from fastapi import FastAPI

app = FastAPI()

pessoa = {'nome': 'Rogério Silva',
          'idade': 38, 'cidade': 'São Paulo'}


@app.get('/')
def hello():
    return 'Hello FastAPI!'


@app.get('/saudacao')
def saudacao():
    return pessoa
