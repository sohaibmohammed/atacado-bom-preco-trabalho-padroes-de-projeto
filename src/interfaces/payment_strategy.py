from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    A interface para as estratégias de pagamento.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Processa o pagamento no valor especificado.
        """
        pass