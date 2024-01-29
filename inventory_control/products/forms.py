from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["thumbnail", "slug", "is_perishable"]
        
        labels = {
            "name": "Nome do Produto",
            "description": "Descrição do Produto",
            "sale_price": "Preço de venda",
            "expiration_date": "Data de expiração",
            "photo": "Imagem do Produto",
            "enabled": "Ativo",
            "category": "Categoria"
        }
        
        error_messages = {
            "name": {
                "required": "O campo nome do produto é obrigatório",
                "unique": "Já existe um produto cadastrado com esse nome",
            },
            "description": {
                "required": "O campo descrição o produto é obrigatório",
            },
            "sale_price": {
                "required": "O campo preço de venda é obrigatório",
            },
        }
        
        widgets = {
            "expiration_date": forms.DateInput(attrs={"type":"date"}, format="%Y-%m-%d")
        }