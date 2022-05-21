import json

from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, Order
from .forms import ProductForm, OrderForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html', {
        'product_list': Product.objects.all()
    })


@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def product_handler(request):
    if request.method == 'POST':
        """
        METHOD TO CREATE A NEW PRODUCT
        """
        data = request.data
        if not data:
            return Response({
                'error': 'body data is required',
                'fields': model_to_dict(Product, fields=['name', 'unitary_value', 'quantity_stock']).keys()})
        try:
            product = Product.objects.create(**data)
            return Response(model_to_dict(product))

        except Exception as err:
            return Response({'error': str(err)})

    if request.method == 'DELETE':
        try:
            data = json.loads(request.body.decode())
            invalid_ids = []
            for prod_id in data['ids']:
                try:
                    product = Product.objects.get(id=prod_id)
                    product.delete()

                except ObjectDoesNotExist:
                    invalid_ids.append(prod_id)

            return Response({'status': 'success', 'deleted': data['ids'], 'invalids': invalid_ids})

        except Exception as err:
            return Response({'erro': 'error to collect data'})

    if request.method == 'PUT':
        try:
            data = request.data
            print(data.values())
            if not data:
                return Response({
                    'error': 'Body data is required',
                    'alert': 'id field is most important',
                    'fields': model_to_dict(Product).keys(),
                })
            try:
                product = Product.objects.get(id=data['id'])
                data.pop('id')
                for key, value in data.items():
                    setattr(product, key, value)
                product.save()

            except ObjectDoesNotExist:
                return Response({'error': 'ID not found'})

            return Response({'ok': '1'})

        except Exception as err:
            print(err)
            return Response({'erro': 'error to collect data'})


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class ListOrders(ListView):
    model = Order
    context_object_name = "order_list"


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            product: Product = form.cleaned_data['product']
            want_qtd = form.cleaned_data['quantity']
            if product.product_situation == 'un':
                return HttpResponse(form.cleaned_data)
            form.save()
    else:
        return render(request, 'orders/order_form.html', {
            'form': OrderForm()
        })

class DetailOrder(DetailView):
    model = Order
