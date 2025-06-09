from src.interfaces import ProductDecorator, Product

class CustomStampDecorator(ProductDecorator):
    """
    Adiciona o custo e a descrição de uma estampa personalizada.
    """
    def __init__(self, product: Product, stamp: str):
        super().__init__(product)
        self._stamp = stamp

    def get_price(self) -> float:
        """Adiciona o valor da estampa ao preço original."""
        return self._product.get_price() + 5.50

    def get_details(self) -> str:
        """Adiciona a informação sobre a estampa aos detalhes."""
        return f"Produto: {self._product.name} (Estampa: '{self._stamp}'), Preço: R${self.get_price():.2f}"