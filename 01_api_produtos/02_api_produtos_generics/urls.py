from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoDetailView,
    ProdutoUpdateView,
    ProdutoDestroyView,
)

urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    path('produtos/criar/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('produtos/<int:pk>/atualizar/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produtos/<int:pk>/deletar/', ProdutoDestroyView.as_view(), name='produto-destroy'),
]