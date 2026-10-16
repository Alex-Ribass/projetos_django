from rest_framework import generics 
from rest_framework.exceptions import ValidationError
from .models import Produto
from .serializer import ProdutoSerializer


class ProdutoListView(generics.ListAPIView):
    serializer_class = ProdutoSerializer

    # Listar apenas os Produtos ativos.
    def get_queryset(self):
        return Produto.objects.filter(ativo=True)

class ProdutoCreateView(generics.CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):

        nome_informado = serializer.validated_data.get('nome')

        if Produto.objects.filter(nome=nome_informado).exists():
            raise ValidationError({"nome": [f'O Produto: {nome_informado} já existe.']})

        serializer.save(ativo=True)

class ProdutoDetailView(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoUpdateView(generics.UpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_update(self, serializer):

        nome_informado = serializer.validated_data.get('nome')

        id_informado = serializer.instance.pk

        if nome_informado:
            nome_existe = Produto.objects.filter(nome=nome_informado).exclude(pk=id_informado).exists()
            if nome_existe:
                raise ValidationError({"nome": [f'O Produto: {nome_informado} já existe.']})

        serializer.save()

class ProdutoDestroyView(generics.DestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_destroy(self, instance):

        instance.delete



