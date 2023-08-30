import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Mocha", 2, 20)
        self.drink2 = Drink("Latte", 4, 30)
        self.drink3 = Drink("Hot Chocolate", 3, 00)
        list_of_drinks = [self.drink1, self.drink2, self.drink3]
        self.coffee_shop = CoffeeShop("Costa", 500, list_of_drinks)
    

    def test_coffee_shop_has_name(self):
        self.assertEqual("Costa", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(20)
        self.assertEqual(520, self.coffee_shop.till)

    def test_if_till_has_been_increased(self):
        self.coffee_shop.increase_till(5)
        self.assertEqual(505, self.coffee_shop.till)

