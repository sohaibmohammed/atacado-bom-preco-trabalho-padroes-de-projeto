from abc import ABC, abstractmethod

class Product(ABC):
    """
    A interface (Protocolo) para os produtos. Define a estrutura comum
    que todos os produtos concretos devem seguir.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self) -> str:
        """Retorna os detalhes do produto."""
        pass