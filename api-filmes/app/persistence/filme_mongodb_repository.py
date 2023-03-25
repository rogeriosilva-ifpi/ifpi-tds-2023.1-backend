from typing import TypedDict

from bson.objectid import ObjectId
from decouple import config
from pymongo import MongoClient

from ..presentation.viewmodels import Filme


class FilmeMongo(TypedDict):
    _id: ObjectId
    nome: str
    genero: str
    ano: int
    duracao: int


class FilmeMongoDBRepository():

    def __init__(self):
        # Connect to MongoDB
        # uri = 'mongodb://localhost:27017'
        uri = config('MONGODB_URL')
        client = MongoClient(uri)
        db = client['filmesapp']
        self.filmes = db['filmes']

        try:
            # print('Info MongoDB Server: ', client.server_info())
            print('MongoDB 💖')
        except Exception:
            print('Deu erro!')

    def todos(self, skip=0, take=0):
        filmes = self.filmes.find().skip(skip).limit(take)
        return list(map(Filme.fromDict, filmes))

    def salvar(self, filme):
        _id = self.filmes.insert_one(filme.toDict()).inserted_id
        filme.id = str(_id)
        return filme

    def obter_um(self, filme_id):
        filtro = {"_id": ObjectId(filme_id)}
        filme_encontrado = self.filmes.find_one(filtro)
        return Filme.fromDict(filme_encontrado) if filme_encontrado else None

    def remover(self, filme_id):
        filtro = {"_id": ObjectId(filme_id)}
        self.filmes.delete_one(filtro)

    def atualizar(self, filme_id, filme):
        filtro = {"_id": ObjectId(filme_id)}
        self.filmes.update_one(filtro, {'$set': filme.toDict()})
        filme.id = filme_id
        return filme
