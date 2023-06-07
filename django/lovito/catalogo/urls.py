from django.urls import path

from .views import ListCategoriaView, ListClasseProdutoView, ListProdutoView

urlpatterns = [
    path('produtos', ListProdutoView.as_view(), name='produto-lista'),
    path('categorias', ListCategoriaView.as_view(), name='categoria-lista'),
    path('classes', ListClasseProdutoView.as_view(), name='classe-produto-lista')
]
