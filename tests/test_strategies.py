import unittest
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.strategies import CreditCardPaymentStrategy, PixPaymentStrategy

class TestPaymentStrategies(unittest.TestCase):
    def test_credit_card_strategy(self):
        """Verifica se a estratégia de cartão de crédito funciona."""
        strategy = CreditCardPaymentStrategy()
        # Captura a saída do print para verificação
        with StringIO() as buffer:
            sys.stdout = buffer
            strategy.process_payment(100.0)
            output = buffer.getvalue()
        self.assertIn("Pagamento de R$100.00 processado com Cartão de Crédito", output)
        sys.stdout = sys.__stdout__ # Restaura a saída padrão
        print(f"\n[PASS] {self.id()}")

    def test_pix_strategy(self):
        """Verifica se a estratégia de Pix aplica o desconto corretamente de 5%."""
        strategy = PixPaymentStrategy()
        with StringIO() as buffer:
            sys.stdout = buffer
            strategy.process_payment(100.0)
            output = buffer.getvalue()
        self.assertIn("Desconto de R$5.00 aplicado", output) #valor de 100
        self.assertIn("Valor final de R$95.00 processado com Pix", output)
        sys.stdout = sys.__stdout__
        print(f"[PASS] {self.id()}")

if __name__ == '__main__':
    unittest.main()