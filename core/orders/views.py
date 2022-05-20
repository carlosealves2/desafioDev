from django.shortcuts import render
from .models import Order, Product


# Create your views here.

def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html', {
        'product_list': Product.objects.all()
    })
