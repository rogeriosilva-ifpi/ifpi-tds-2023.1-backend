from django.urls import path

from .views import ListCategoriaView, ListClasseProdutoView

urlpatterns = [
    path('categorias', ListCategoriaView.as_view(), name='categoria-lista'),
    path('classes', ListClasseProdutoView.as_view(), name='classe-produto-lista')
]
