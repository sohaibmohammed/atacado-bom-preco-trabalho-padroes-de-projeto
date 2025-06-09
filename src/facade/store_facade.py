from typing import Literal, Dict, Type
from src.interfaces import Product, ProductFactory
from src.factories import SchoolSupplyFactory, ToyFactory, UtilityFactory
from src.decorators import GiftWrapDecorator, CustomStampDecorator

class StoreFacade:
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

    def buy_product(
        self,
        product_type: Literal['material_escolar', 'brinquedo', 'utilidade'],
        name: str,
        price: float,
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

        print(f"Compra finalizada: {product.get_details()}")
        return product