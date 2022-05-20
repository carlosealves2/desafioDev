from django.forms import ModelForm
from django import forms
from .models import Product


class ProductForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    unitary_value = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    quantity_stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    class Meta:
        model = Product
        fields = ['name', 'unitary_value', 'quantity_stock']
