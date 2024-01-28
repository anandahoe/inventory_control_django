from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        
        error_messages = {
            "company_name": {
                "unique": "A razão social já existe"
            }
        }
    
        error_messages = {
            "fantasy_name": {
                "unique": "O nome fantasia já existe"
            }
        }
        
        error_messages = {
            "cnpj": {
                "unique": "O CNPJ já existe"
            }
        }
        
        error_messages = {
            "email": {
                "unique": "O e-mail já existe"
            }
        }
        