from django.urls import path
from .views import ProdutoListCreateAPIView, ProdutoDetailAPIView

urlpatterns = [
    path('produtos/', ProdutoListCreateAPIView.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', ProdutoDetailAPIView.as_view(), name='produto-detail'),
]