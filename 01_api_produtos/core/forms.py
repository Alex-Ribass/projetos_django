from django import forms
from .models import EntradaDiario 

class DiarioForm(forms.ModelForm):
    class Meta:
        model = EntradaDiario 
        fields = ['titulo', 'conteudo']

        labels = {
            'titulo': 'Título da Memória',
            'conteudo': 'O que aconteceu hoje?',
        }