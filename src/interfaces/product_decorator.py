from .product import Product
from abc import ABC

class ProductDecorator(Product, ABC):
    """
    O Decorator base abstrato. Ele segue a mesma interface do Produto
    e contém uma referência para o objeto Produto que ele envolve.
    """
    def __init__(self, product: Product):
        # O nome e o preço são inicialmente herdados do produto embrulhado.
        # As subclasses de decorador podem modificar esses valores.
        super().__init__(product.name, product.price)
        self._product = product