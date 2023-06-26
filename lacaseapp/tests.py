import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Cart, Orders

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Apple", description="Fresh apple", price=1.99)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Apple")
        self.assertEqual(self.product.description, "Fresh apple")
        self.assertEqual(self.product.price, 1.99)

    def test_product_required_fields(self):
        with self.assertRaises(Exception):
            Product.objects.create(name="", description="", price=None)

    def test_product_save(self):
        product = Product(name="Banana", description="Fresh banana", price=0.99)
        product.save()
        saved_product = Product.objects.get(name="Banana")
        self.assertEqual(saved_product, product)

class CartTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Orange", description="Fresh orange", price=2.49)
        self.cart = Cart.objects.create()

    def test_cart_total(self):
        self.cart.add_product(self.product, quantity=2)
        self.assertEqual(self.cart.total, 4.98)

    def test_cart_product_addition(self):
        self.cart.add_product(self.product, quantity=3)
        self.assertEqual(self.cart.products.count(), 1)

    def test_cart_product_removal(self):
        self.cart.add_product(self.product, quantity=1)
        self.cart.remove_product(self.product)
        self.assertEqual(self.cart.products.count(), 0)

class OrdersTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Pear", description="Fresh pear", price=1.49)
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.orders = Orders.objects.create(user=self.user)

    def test_orders_creation(self):
        self.assertEqual(self.orders.user, self.user)

    def test_orders_required_fields(self):
        with self.assertRaises(Exception):
            Orders.objects.create(user=None)

class SearchTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Grapes", description="Fresh grapes", price=3.99)
        Product.objects.create(name="Strawberry", description="Fresh strawberry", price=2.99)

    def test_product_search_exact_match(self):
        results = Product.objects.filter(name="Grapes")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Grapes")

    def test_product_search_partial_match(self):
        results = Product.objects.filter(name__icontains="berry")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Strawberry")

#class StockTestCase(TestCase):
#    def setUp(self):
#        self.product = Product.objects.create(name="Mango", description="Fresh mango", price=4.99, stock=10)
#
#    def test_product_quantity_update_after_order(self):
#        order = Order.objects.create(user=User.objects.create_user(username="testuser", password="testpassword"))
#        order.add_product(self.product, quantity=5)
#        self.product.refresh_from_db()
#        self.assertEqual(self.product.stock, 5)
#
#    def test_out_of_stock_product_display(self):
#        self.product.stock = 0
#        self.product.save()
#        response = self.client.get('/products/')
#        self.assertContains(response, "Out of stock", status_code=200)

#class PromotionTestCase(TestCase):
#    def setUp(self):
#        self.product = Product.objects.create(name="Pineapple",





