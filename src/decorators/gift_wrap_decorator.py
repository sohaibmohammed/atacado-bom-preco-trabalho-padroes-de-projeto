from src.interfaces import ProductDecorator

class GiftWrapDecorator(ProductDecorator):
    """
    Adiciona o custo e a descrição do embrulho de presente a um produto.
    """
    def get_price(self) -> float:
        """Adiciona o valor do embrulho ao preço original."""
        return self._product.get_price() + 10.00

    def get_details(self) -> str:
        """Adiciona a informação sobre o embrulho aos detalhes."""
        # Note que aqui estamos pegando o nome do produto original (_product.name)
        # e o preço final deste decorador (self.get_price()).
        return f"Produto: {self._product.name} (Embrulhado para Presente), Preço: R${self.get_price():.2f}"