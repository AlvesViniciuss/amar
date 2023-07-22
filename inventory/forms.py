# inventory/forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['data', 'modelo', 'cor', 'tamanho', 'valor', 'valor_venda', 'quantidade', ]
