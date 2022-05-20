from django.urls import path
from .views import *

app_name = "app"
urlpatterns = [
    path('', index, name="home"),
    path('/products', products, name="products"),
    path('product/', product_handler, name="product_handle"),
]