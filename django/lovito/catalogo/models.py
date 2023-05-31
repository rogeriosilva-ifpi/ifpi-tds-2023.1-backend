from django.db import models


class AbstractBaseModel(models.Model):
    criado_em = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(
        verbose_name='Criado em', auto_now=True)

    class Meta:
        abstract = True


class Categoria(AbstractBaseModel):
    nome = models.CharField(verbose_name='Nome',
                            max_length=128, null=False, blank=False)

    def __str__(self):
        return self.nome


class ClasseProduto(AbstractBaseModel):
    nome = models.CharField(verbose_name='Classe',
                            max_length=64, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Classe de Produtos'

    def __str__(self):
        return self.nome

    # autocomplete do admin
    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'nome__icontains')


class Produto(AbstractBaseModel):
    nome = models.CharField(verbose_name='Nome',
                            null=False, blank=False, max_length=30)
    descricao = models.TextField(
        verbose_name='Descrição', null=False, blank=False, max_length=255)
    preco = models.DecimalField(
        max_digits=8, decimal_places=2, help_text='em R$')
    ativo = models.BooleanField(
        verbose_name='Ativo?', default=True, help_text='Só é possível vender produtos ativos')

    # relacionamentos
    classe = models.ForeignKey(
        ClasseProduto, on_delete=models.PROTECT, null=True, related_name='produtos')

    def __str__(self):
        return self.nome


class CategoriaProduto(AbstractBaseModel):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, related_name='categorias')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias de Produto'

    def __str__(self):
        return f'{self.produto} --> {self.categoria}'


class AtributoClasseProduto(AbstractBaseModel):
    classe = models.ForeignKey(
        ClasseProduto, on_delete=models.PROTECT, related_name='atributos')
    nome = models.CharField(
        verbose_name='Nome Atributo', max_length=24, null=False, blank=False)


class ValorAtributoClasseProduto(AbstractBaseModel):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='atributos')
    atributo = models.ForeignKey(
        AtributoClasseProduto, on_delete=models.PROTECT)
    valor = models.CharField(verbose_name='Valor',
                             max_length=255, null=False, blank=False)


class ImagemProduto(AbstractBaseModel):
    nome = models.CharField(
        verbose_name='Nome da Imagem', null=False, blank=False)
    ordem = models.PositiveSmallIntegerField(
        verbose_name='Ordem de exibição', default=0)
    arquivo = models.ImageField(verbose_name='Arquivo')

    # relacionamento
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='imagens')
