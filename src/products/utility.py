from src.interfaces import Product

class Utility(Product):
    """Representa um produto do tipo Utilidade."""
    def get_details(self) -> str:
        return f"Utilidade: {self.name}, Preço: R${self.price:.2f}"