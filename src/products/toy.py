from src.interfaces import Product

class Toy(Product):
    """Representa um produto do tipo Brinquedo."""
    def get_details(self) -> str:
        return f"Brinquedo: {self.name}, Preço: R${self.price:.2f}"