import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 3, "30")

    def test_if_drink_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_if_drink_has_price(self):
        self.assertEqual(3, self.drink.price)

    def test_if_drink_has_caffeine_level(self):
        self.assertEqual("30", self.drink.caffeine_level)