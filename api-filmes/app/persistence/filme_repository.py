class FilmeInMemoryRepository():

    def __init__(self):
        self.filmes = []
        self.proximo_id = 1

    def todos(self, skip, take):
        inicio = skip

        if skip and take:
            fim = skip + take
        else:
            fim = None

        return self.filmes[inicio:fim]

    def salvar(self, filme):
        filme.id = self.proximo_id
        self.proximo_id += 1
        self.filmes.append(filme)

        return filme

    def obter_um(self, filme_id):
        for filme in self.filmes:
            if filme.id == filme_id:
                return filme

        return None

    def remover(self, filme_id):
        filme = self.obter_um(filme_id)
        if filme:
            self.filmes.remove(filme)

    def atualizar(self, filme_id, filme):
        for index in range(len(self.filmes)):
            filme_atual = self.filmes[index]
            if filme_atual.id == filme_id:
                filme.id = filme_atual.id
                self.filmes[index] = filme
                return filme
