Resource: Filme ("filmes")
EndPoints da API REST
BaseURL: http://127.0.0.1:8000

METHOD  URL             PAYLOAD     DESCRIPTION
---
GET     /filmes         False       Get All
GET     /filmes/123     False       Get One (123)
POST    /filmes         True        Create Resource
DELETE  /filmes/123     False       Delete One (123)
PUT     /filmes/123     True        Update One (123)
PATCH   /filmes/123     True        Partial Update One(123)