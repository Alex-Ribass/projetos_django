from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Produto
from .serializer import ProdutoSerializer

class ProdutoListCreateAPIView(APIView):

    serializer_class = ProdutoSerializer 

    def get (self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProdutoDetailAPIView(APIView):

    serializer_class = ProdutoSerializer

    def get (self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        serializer = ProdutoSerializer(produto)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        produto = get_object_or_404 (Produto, pk=pk)
        serializer = ProdutoSerializer(produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        produto.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    

    