from abc import ABC, abstractmethod
from .product import Product

class ProductFactory(ABC):
    """
    A classe Creator abstrata. Declara o Factory Method que deve
    retornar um objeto de uma classe Produto.
    """

    @abstractmethod
    def factory_method(self, name: str, price: float) -> Product:
        """Este é o método de fábrica que as subclasses irão implementar."""
        pass

    def create_product(self, name: str, price: float) -> Product:
        """
        Este é o método principal que o cliente usará. Ele utiliza o
        factory_method para criar o produto.
        """
        product = self.factory_method(name, price)
        return product