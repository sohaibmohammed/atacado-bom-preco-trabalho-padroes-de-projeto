from src.interfaces.observer_protocol import Observer
from src.interfaces import Product

class EmailObserver(Observer):
    """Observa as vendas e simula o envio de um e-mail de confirmação."""
    def update(self, data: Product) -> None:
        if isinstance(data, Product):
            product_details = data.get_details()
            print(f"[OBSERVER DE E-MAIL]: Enviando e-mail de confirmação para o cliente sobre a compra: {product_details}")