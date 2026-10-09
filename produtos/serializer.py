from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


    def validate_nome(self, value):

        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError('O campo Nome só deve conter letras.')
        return value 
    def validate_preco(self, value):

        if value <=0:
            raise serializers.ValidationError('Não aceita valor menor ou igual a 0 ')
        return value 
    
    def validate_quantidade(self, value):
    
        if value <=0:
            raise serializers.ValidationError('Não aceita Quantidade menor ou igual a 0')
        return value 
    