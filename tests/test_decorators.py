import unittest

# Adiciona o diretório raiz do projeto ao path para importação dos módulos
#resolve erro de importacao de modulos (em outra pasta)
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.products.toy import Toy
from src.decorators import GiftWrapDecorator, CustomStampDecorator

class TestProductDecorators(unittest.TestCase):
    def test_gift_wrap_decorator(self):
        """Testa se o decorator de embrulho para presente funciona."""
        toy = Toy("Lego", 150.00)
        wrapped_toy = GiftWrapDecorator(toy)

        self.assertEqual(wrapped_toy.get_price(), 160.00) # 150 + 10
        self.assertIn("(Embrulhado para Presente)", wrapped_toy.get_details())
        print(f"\n[PASS] {self.id()}")

    def test_custom_stamp_decorator(self):
        """Testa se o decorator de estampa funciona."""
        toy = Toy("Lego", 150.00)
        stamped_toy = CustomStampDecorator(toy, stamp="Feliz Aniversário!")

        self.assertAlmostEqual(stamped_toy.get_price(), 155.50) # 150 + 5.50
        self.assertIn("(Estampa: 'Feliz Aniversário!')", stamped_toy.get_details())
        print(f"[PASS] {self.id()}")

    def test_stacked_decorators(self):
        """Testa o empilhamento de múltiplos decorators."""
        toy = Toy("Quebra-cabeça", 80.00)
        
        # Aplica os dois decorators
        stamped_toy = CustomStampDecorator(toy, stamp="Boas Festas")
        final_product = GiftWrapDecorator(stamped_toy)

        # Preço final = 80 (base) + 5.50 (estampa) + 10.00 (embrulho)
        self.assertAlmostEqual(final_product.get_price(), 95.50)
        self.assertIn("(Embrulhado para Presente)", final_product.get_details())
        # O detalhe final do embrulho sobrescreve o da estampa, mas o preço é acumulado.
        # Isso mostra com aordem dos decorators importa.
        print(f"[PASS] {self.id()}")

if __name__ == '__main__':
    unittest.main()