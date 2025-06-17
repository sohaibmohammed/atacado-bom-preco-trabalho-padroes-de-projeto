from src.interfaces import PaymentStrategy

class CreditCardPaymentStrategy(PaymentStrategy):
    """
    Estratégia para processar pagamentos com Cartão de Crédito.
    """
    def process_payment(self, amount: float) -> None:
        # Lógica de processamento de cartão de crédito...
        print(f"Pagamento de R${amount:.2f} processado com Cartão de Crédito.")