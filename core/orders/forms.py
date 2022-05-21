from django.forms import ModelForm
from django import forms
from .models import Product, Order


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


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for vfield in self.visible_fields():
            if vfield.field.label == 'Product':
                vfield.field.widget.attrs['class'] = 'form-select'
            else:
                vfield.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Order
        fields = '__all__'
