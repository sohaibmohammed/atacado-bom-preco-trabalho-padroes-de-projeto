from src.interfaces import PaymentStrategy

class PixPaymentStrategy(PaymentStrategy):
    """
    Estratégia para processar pagamentos com Pix.
    Poderia, por exemplo, aplicar um desconto.
    """
    def process_payment(self, amount: float) -> None:
        discount = amount * 0.05 # 5% de desconto no Pix
        final_amount = amount - discount
        print(f"Pagamento com Pix. Desconto de R${discount:.2f} aplicado.")
        print(f"Valor final de R${final_amount:.2f} processado com Pix.")