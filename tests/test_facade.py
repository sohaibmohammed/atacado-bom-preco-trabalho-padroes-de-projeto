import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.facade import StoreFacade
from src.products.toy import Toy
from src.products.utility import Utility
from src.decorators import GiftWrapDecorator

class TestStoreFacade(unittest.TestCase):
    def setUp(self):
        """Configura a facade antes de cada teste."""
        self.facade = StoreFacade()

    def test_buy_simple_product(self):
        """Testa a compra de um produto simples via facade."""
        product = self.facade.buy_product("brinquedo", "Action Figure", 75.00)
        self.assertIsInstance(product, Toy)
        self.assertEqual(product.price, 75.00)
        print(f"\n[PASS] {self.id()}")

    def test_buy_product_with_gift_wrap(self):
        """Testa a compra com o decorator de embrulho."""
        product = self.facade.buy_product(
            "utilidade", "Garrafa Térmica", 50.00, add_gift_wrap=True
        )
        # O objeto retornado é a camada mais externa do decorator
        self.assertIsInstance(product, GiftWrapDecorator)
        self.assertEqual(product.get_price(), 60.00) # 50 + 10
        print(f"[PASS] {self.id()}")

    def test_buy_product_with_all_decorators(self):
        """Testa a compra com múltiplos decorators via facade."""
        product = self.facade.buy_product(
            "material_escolar", "Mochila", 120.00,
            add_gift_wrap=True,
            custom_stamp="Para meu filho"
        )
        self.assertEqual(product.get_price(), 135.50) # 120 + 10 + 5.50
        print(f"[PASS] {self.id()}")

    def test_invalid_product_type(self):
        """Testa se a facade levanta um erro para tipo de produto inválido."""
        with self.assertRaises(ValueError):
            self.facade.buy_product("eletronico", "Fone de ouvido", 200.00)
        print(f"[PASS] {self.id()}")

if __name__ == '__main__':
    unittest.main()