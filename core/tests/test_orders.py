from django.test import TestCase

from orders.models import Product


class ProductTestCase(TestCase):
    def setUp(self) -> None:
        Product.objects.create(name="Smartphone X Mark 2022", unitary_value=2635.33, quantity_stock=8)
        Product.objects.create(name="headphones Atomic buster", unitary_value=256.99, quantity_stock=1)
        Product.objects.create(name="eletric toothbrush", unitary_value=89.9, quantity_stock=0)
        Product.objects.create(name="remote control car", unitary_value=50, quantity_stock=2)
        Product.objects.create(name="", unitary_value=0, quantity_stock=0)

    def test_avalability_of_products(self):
        prod1 = Product.objects.get(name="Smartphone X Mark 2022")
        self.assertEqual(prod1.product_situation, "av")

        prod2 = Product.objects.get(name="eletric toothbrush")
        self.assertEqual(prod2.product_situation, "un")

    def test_validating_models(self):
        prod1 = Product.objects.get(name="Smartphone X Mark 2022")
        self.assertEqual(float(prod1.unitary_value), 2635.33)
        self.assertEqual(prod1.quantity_stock, 8)

        prod2 = Product.objects.get(name="")
        self.assertEqual(float(prod2.unitary_value), 0)
        self.assertEqual(prod2.quantity_stock, 0)

