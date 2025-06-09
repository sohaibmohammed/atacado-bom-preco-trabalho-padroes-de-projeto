from src.interfaces import Product

class SchoolSupply(Product):
    """Representa um produto do tipo Material Escolar."""
    def get_details(self) -> str:
        return f"Material Escolar: {self.name}, Preço: R${self.price:.2f}"