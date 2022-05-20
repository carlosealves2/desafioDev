from django.urls import path
from .views import *

app_name = "app"
urlpatterns = [
    path('', index, name="home"),
    path('products/', products, name="products"),
    path('product/', product_handler, name="product_handle"),
    path('product/<int:pk>', ProductUpdateView.as_view(), name="product_update"),
    path('new-product/', CreateProductView.as_view(), name="new_product"),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]