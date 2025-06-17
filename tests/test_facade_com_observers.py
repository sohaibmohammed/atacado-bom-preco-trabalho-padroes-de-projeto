import unittest
import sys
import os
from unittest.mock import Mock

# Garante que o Python encontre os módulos do projeto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.facade import StoreFacade
from src.interfaces import Observer
from src.observers import InventoryObserver, EmailObserver
from src.strategies import CreditCardPaymentStrategy
from src.interfaces import Product 

class TestFacadeBehavior(unittest.TestCase):
    def test_facade_notifies_observers_with_correct_data(self):
        """
        Verifica se a facade notifica os observadores com o produto correto
        após uma compra bem-sucedida.
        """

        facade = StoreFacade()
        payment_strategy = CreditCardPaymentStrategy()
        
        # Criamos Mocks (dublês) para os observadores.
        # Usar spec=Observer garante que o mock só aceite métodos da interface Observer
        mock_inventory_observer = Mock(spec=Observer)
        mock_email_observer = Mock(spec=Observer)

        # Anexamos os observadores mockados na facade
        facade.attach(mock_inventory_observer)
        facade.attach(mock_email_observer)

        # 1. Realizamos a compra e pegamos o produto retornado
        sold_product = facade.buy_product(
            product_type='brinquedo',
            name='Lego Star Wars',
            price=350.00,
            payment_strategy=payment_strategy
        )

        # 2. Vendo se o produto foi criado com sucesso (não é None)
        self.assertIsNotNone(sold_product)
        self.assertIsInstance(sold_product, Product)

        # 3. Verificamos se o método 'update' de cada observador foi chamado uma vez 
        # com o produto passado como argumento.
        mock_inventory_observer.update.assert_called_once_with(sold_product)
        mock_email_observer.update.assert_called_once_with(sold_product)
        
        print(f"\n[PASS] {self.id()}")

if __name__ == '__main__':
    unittest.main()