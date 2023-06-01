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
                    'preco', 'classe', 'nomes_categorias']
    list_filter = ['ativo', 'classe']

    search_fields = ['nome', 'descricao']

    date_hierarchy = 'criado_em'

    inlines = [CategoriaProdutoInline]

    # Django nativo: autocomplete
    # autocomplete_fields = ['classe']

    # Grappelli: autocomplete
    raw_id_fields = ('classe',)
    autocomplete_lookup_fields = {
        'fk': ['classe']
    }

    # @admin.display(description='Categorias')
    # def nomes_categorias(self, produto):
    #     categorias = produto.categorias.all()
    #     nomes_categorias = [c.categoria.nome for c in categorias]
    #     return ', '.join(nomes_categorias) if len(categorias) > 0 else 7 * '-'

    # Grappelli - Filter in a sidebar
    change_list_template = 'admin/change_list_filter_sidebar.html'
    # change_list_template = 'admin/change_list_filter_confirm_sidebar.html'

    change_list_filter_template = 'admin/filter_listing.html'


@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(ClasseProduto)
class ClasseProdutoAdmin(admin.ModelAdmin):

    search_fields = ['nome']
