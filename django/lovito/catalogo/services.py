from .models import Categoria, Produto


class ProdutoService():

    def ativos(self):
        return Produto.objects.filter(ativo=True)


class CategoriaService():

    def obter_ordenado(self, campo='criado_em', inverso=False):
        ordenado_por = campo if inverso == False else f'-{campo}'
        return Categoria.objects.all().order_by(ordenado_por)
