import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 30, 17, 50)
        

    def test_if_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)

    def test_if_customer_has_wallet(self):
        self.assertEqual(30, self.customer.wallet)

    def test_if_wallet_has_been_reduced(self):
        self.customer.reduce_wallet(5)
        self.assertEqual(25, self.customer.wallet)

    def test_if_customer_has_age(self):
        self.assertEqual(17, self.customer.age)
