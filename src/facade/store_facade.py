from typing import Literal, Dict, Type, List
from src.interfaces.product import Product
from src.interfaces.product_factory import ProductFactory
from src.factories import SchoolSupplyFactory, ToyFactory, UtilityFactory
from src.decorators import GiftWrapDecorator, CustomStampDecorator
from src.interfaces.payment_strategy import PaymentStrategy
from src.interfaces import Observer, Subject

class StoreFacade(Subject):
    """
    Fornece uma interface simples para as operações complexas da loja,
    como criar e decorar produtos.
    """
    def __init__(self):
        self._factories: Dict[str, Type[ProductFactory]] = {
            'material_escolar': SchoolSupplyFactory,
            'brinquedo': ToyFactory,
            'utilidade': UtilityFactory,
        }
        self._observers: List[Observer] = []
        self.last_product_sold: Product | None = None

    # Métodos do padrão Observer
    def attach(self, observer: Observer) -> None:
        print(f"Facade: Anexando o observador {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Facade: Notificando observadores com os dados do produto...")
        for observer in self._observers:
            # Envia o produto vendido como dado para o observer
            observer.update(self.last_product_sold)

    def buy_product(
        self,
        product_type: Literal['material_escolar', 'brinquedo', 'utilidade'],
        name: str,
        price: float,
        payment_strategy: PaymentStrategy, # <-- Estratégia de pagamento
        *, # Argumentos abaixo são apenas por keyword
        add_gift_wrap: bool = False,
        custom_stamp: str | None = None
    ) -> Product:
        """
        Cria e, opcionalmente, decora um produto.

        Args:
            product_type: O tipo de produto a ser criado.
            name: O nome do produto.
            price: O preço base do produto.
            add_gift_wrap: Se deve embrulhar para presente.
            custom_stamp: A estampa a ser adicionada.

        Returns:
            O objeto Produto final, possivelmente decorado.
        """
        if product_type not in self._factories:
            raise ValueError(f"Tipo de produto inválido: {product_type}")

        # 1. Usa a fábrica apropriada para criar o produto base
        factory = self._factories[product_type]()
        product = factory.create_product(name, price)

        # 2. Aplica os decoradores, se solicitado
        if add_gift_wrap:
            product = GiftWrapDecorator(product)
        
        if custom_stamp:
            product = CustomStampDecorator(product, stamp=custom_stamp)

        # 3. Usa a Strategy para processar o pagamento
        try:
            payment_strategy.process_payment(product.get_price())
        except Exception as e:
            print(f"Ocorreu um erro no pagamento: {e}")
            return None

        # 4. Se o pagamento foi bem-sucedido, notifica os Observers
        self.last_product_sold = product
        print(f"Compra finalizada: {product.get_details()}")
        self.notify()
        
        return product