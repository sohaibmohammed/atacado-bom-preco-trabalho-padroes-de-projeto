from src.interfaces.observer_protocol import Observer
from src.interfaces import Product

class InventoryObserver(Observer):
    """Observa as vendas e simula a atualização do estoque."""
    def update(self, data: Product) -> None:
        if isinstance(data, Product):
            print(f"[OBSERVER DE ESTOQUE]: Venda de '{data.name}' registrada. Atualizando inventário...")