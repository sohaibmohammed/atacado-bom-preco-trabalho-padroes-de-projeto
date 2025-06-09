from src.interfaces import ProductFactory, Product
from src.products.toy import Toy

class ToyFactory(ProductFactory):
    """Fábrica concreta para criar produtos do tipo Brinquedo."""
    def factory_method(self, name: str, price: float) -> Product:
        return Toy(name, price)