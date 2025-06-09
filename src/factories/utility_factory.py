from src.interfaces import ProductFactory, Product
from src.products.utility import Utility

class UtilityFactory(ProductFactory):
    """Fábrica concreta para criar produtos do tipo Utilidade."""
    def factory_method(self, name: str, price: float) -> Product:
        return Utility(name, price)