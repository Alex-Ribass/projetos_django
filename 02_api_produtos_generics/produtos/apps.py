from django.apps import AppConfig

class ApiProdutosGenericsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'
    label = 'produtos_generics'  # <--- Este é o segredo! O Django usa este nome interno, ignorando o número da pasta.