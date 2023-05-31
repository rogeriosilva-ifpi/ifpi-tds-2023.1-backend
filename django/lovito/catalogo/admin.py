from django.contrib import admin

from catalogo.models import Categoria, CategoriaProduto, ClasseProduto, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

    list_display = ['nome', 'criado_em', 'atualizado_em']


class CategoriaProdutoInline(admin.TabularInline):
    model = CategoriaProduto
    # max_num = 2
    extra = 1
    classes = ('grp-collapse grp-closed',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Dados Básicos',
         {
             'fields': ['nome', 'descricao']
         }
         ),
        ('Ativação',
         {
             'classes': ('grp-collapse grp-closed',),
             'fields': ['ativo']
         }),
        ('Precificação',
         {
             'classes': ('grp-collapse grp-open',),
             'fields': ['preco']
         }),
        ('Classe do Produto',
         {
             'classes': ('grp-collapse grp-open',),
             'fields': ['classe'],
             'description': 'Cada produto pertence apenas a uma classe'
         })
    ]

    list_display = ['nome', 'ativo', 'descricao',
                    'preco', 'classe']
    list_filter = ['ativo', 'classe']

    search_fields = ['nome', 'descricao']

    inlines = [CategoriaProdutoInline]


@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(ClasseProduto)
class ClasseProdutoAdmin(admin.ModelAdmin):
    pass
