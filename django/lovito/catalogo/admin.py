from django.contrib import admin

from catalogo.models import Categoria, CategoriaProduto, ClasseProduto, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

    list_display = ['nome', 'criado_em', 'atualizado_em']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'descricao', 'preco']


@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(ClasseProduto)
class ClasseProdutoAdmin(admin.ModelAdmin):
    pass
