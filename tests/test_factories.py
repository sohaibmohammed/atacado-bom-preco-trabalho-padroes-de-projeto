import unittest

# Adiciona o diretório raiz do projeto ao path para importação dos módulos
#resolve erro de importacao de modulos (em outra pasta)
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from src.factories import SchoolSupplyFactory, ToyFactory, UtilityFactory
from src.products.school_supply import SchoolSupply
from src.products.toy import Toy
from src.products.utility import Utility

class TestProductFactories(unittest.TestCase):

    def test_school_supply_factory_creates_correct_product(self):
        """Verifica se a SchoolSupplyFactory cria uma instância de SchoolSupply."""
        factory = SchoolSupplyFactory()
        product = factory.create_product("Caderno", 25.50)
        
        self.assertIsInstance(product, SchoolSupply, "O produto deveria ser uma instância de SchoolSupply")
        self.assertEqual(product.name, "Caderno")
        self.assertEqual(product.price, 25.50)
        self.assertEqual(product.get_details(), "Material Escolar: Caderno, Preço: R$25.50")
        print(f"\n\n[PASS] {self.id()}")


    def test_toy_factory_creates_correct_product(self):
        """Verifica se a ToyFactory cria uma instância de Toy."""
        factory = ToyFactory()
        product = factory.create_product("Carrinho de Controle Remoto", 150.00)

        self.assertIsInstance(product, Toy, "O produto deveria ser uma instância de Toy")
        self.assertEqual(product.name, "Carrinho de Controle Remoto")
        self.assertEqual(product.price, 150.00)
        self.assertEqual(product.get_details(), "Brinquedo: Carrinho de Controle Remoto, Preço: R$150.00")
        print(f"\n\n[PASS] {self.id()}")


    def test_utility_factory_creates_correct_product(self):
        """Verifica se a UtilityFactory cria uma instância de Utility."""
        factory = UtilityFactory()
        product = factory.create_product("Garrafa Térmica", 75.99)

        self.assertIsInstance(product, Utility, "O produto deveria ser uma instância de Utility")
        self.assertEqual(product.name, "Garrafa Térmica")
        self.assertEqual(product.price, 75.99)
        self.assertEqual(product.get_details(), "Utilidade: Garrafa Térmica, Preço: R$75.99")
        print(f"\n\n[PASS] {self.id()}")

if __name__ == '__main__':
    unittest.main()