from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    min_price = forms.IntegerField(
        label = "Min price", 
        required = False, 
        widget = forms.TextInput(attrs = {"class": "min-price"})
    )
    max_price = forms.IntegerField(
        label = "Max price", 
        required = False,
        widget = forms.TextInput(attrs = {"class": "max-price"})
    )