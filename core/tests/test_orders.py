from django.test import TestCase

from orders.models import Product, Order


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


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        prod = Product.objects.create(name="Smartphone X Mark 2022", unitary_value=2635.33, quantity_stock=8)
        Order.objects.create(
            product=prod,
            quantity=12,
            unitary_value=2023.39,
            applicant="client 01",
            zip_code=55567505,
            uf="AZ",
            city="city of abc",
            district="zone 0002",
            street="street of news",
            number=100,
            forwarding_agent="agent 001",
        )

    def test_model_values(self):
        order = Order.objects.get(applicant="client 01")
        self.assertEqual(order.product.id, 1)
        self.assertEqual(order.quantity, 12)
        self.assertEqual(float(order.unitary_value), 2023.39)
        self.assertEqual(order.applicant, "client 01")
        self.assertEqual(order.zip_code, 55567505)
        self.assertEqual(order.uf, "AZ")
        self.assertEqual(order.city, "city of abc")
        self.assertEqual(order.district, "zone 0002")
        self.assertEqual(order.street, "street of news")
        self.assertEqual(order.number, 100)
        self.assertEqual(order.forwarding_agent, "agent 001")
        self.assertEqual(order.order_situation, "p")

    def test_order_situation(self):
        order = Order.objects.get(applicant="client 01")
        self.assertEqual(order.order_situation, "p")
        order.order_situation = 's'
        self.assertEqual(order.order_situation, "s")
        order.order_situation = 'd'
        self.assertEqual(order.order_situation, "d")
