from django import forms
from .models import Product
import re

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
        error_messages = {
            "company_name": {
                "unique": "A razão social já existe",
                "max_length": "O tamanho máximo da razão social são 255 caracteres",
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
    
    #Clean nome campo
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get("cnpj", "")
        
        #Removendo valores não numéricos    
        cnpj = re.sub("[^0-9]", "", cnpj)
        return cnpj
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        
        #Removendo valores não numéricos    
        phone = re.sub("[^0-9]", "", phone)
        return phone
    
    def clean_zipcode(self):
        zipcode = self.cleaned_data.get("zipcode", "")
        
        #Removendo valores não numéricos    
        zipcode = re.sub("[^0-9]", "", zipcode)
        return zipcode