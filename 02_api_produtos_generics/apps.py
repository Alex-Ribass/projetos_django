from django.apps import AppConfig

class ApiProdutosGenericsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '02_api_produtos_generics'
    label = 'produtos_generics'  # <--- Este é o segredo! O Django usa este nome interno, ignorando o número da pasta.