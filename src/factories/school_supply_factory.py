from src.interfaces import ProductFactory, Product
from src.products.school_supply import SchoolSupply

class SchoolSupplyFactory(ProductFactory):
    """Fábrica concreta para criar produtos do tipo Material Escolar."""
    def factory_method(self, name: str, price: float) -> Product:
        return SchoolSupply(name, price)