# Projeto Atacado Bom Preco - Padrões de Projeto - Projeto 3 - Final

Neste projeto final, conforme solicitado, foi usado padrões comportamentais, como `Strategy` e `Observer`, visando gerenciar os algoritmos e a comunicação entre os objetos de forma limpa e desacoplada.

O **Strategy** foi usado para gerenciar os diferentes métodos de pagamento. Em vez de uma lógica condicional para "Cartão de Crédito", "Pix", etc., criamos uma interface `PaymentStrategy` e implementamos clssses concretas (`CreditCardPaymentStrategy`, `PixPaymentStrategy`). Assim, o algoritmo de pagamento é escolhido e trocado em tempo de execução, e novos métodos podem ser adicionados sem alterar a StoreFacade.

Ja o padrão **Observer** foi implementado para permitir a notificação de diferentes partes do sistema sobre uma venda, de forma desacoplada. A `StoreFacade` atua como `Subject` (ou "Observável"). Quando uma compra é concluída, ela notifica todos os Observers registrados (como `InventoryObserver` e `EmailObserver`) sem precisar conhecê-los diretamente. Isso permite que novas ações de "pós-venda" sejam adicionadas simplesmente criando novos observadores.

## Exemplo de uso dos padroes

O código abaixo demonstra como os padrões trabalham juntos através da StoreFacade, o ponto de entrada principal do sistema.

```python
from src.facade import StoreFacade
from src.strategies import PixPaymentStrategy, CreditCardPaymentStrategy
from src.observers import InventoryObserver, EmailObserver

# 1. Configuração inicial do sistema
loja = StoreFacade()

# Anexando observadores (padrão Observer) que serão notificados após cada compra
loja.attach(InventoryObserver())
loja.attach(EmailObserver())

# Criando as estratégias de pagamento (padrão Strategy)
estrategia_pix = PixPaymentStrategy()
estrategia_cartao = CreditCardPaymentStrategy()

# 2. Cenário de Compra 1: Produto decorado, pago com Pix
print("--- Cenário 1: Compra de brinquedo decorado com Pix ---")
# A Facade coordena tudo:
# - Usa a Factory de brinquedos para criar o 'Super Robô'.
# - Aplica os Decorators de embrulho e estampa.
# - Usa a Strategy de Pix para processar o pagamento.
# - Notifica os Observers sobre a venda.
loja.buy_product(
    product_type='brinquedo',
    name='Super Robô',
    price=200.00,
    payment_strategy=estrategia_pix, 
    add_gift_wrap=True,
    custom_stamp="Para o melhor filho!"
)

# 3. Cenário de Compra 2: Produto simples, pago com Cartão de Crédito
print("\n--- Cenário 2: Compra de utilidade simples com Cartão ---")
loja.buy_product(
    product_type='utilidade',
    name='Garrafa de Água Inox',
    price=40.00,
    payment_strategy=estrategia_cartao
)
```

# Projeto Atacado Bom Preco - Padrões de Projeto - Projeto 2

Nesta fase, foi adicionado dois padrões estruturais para aumentar a flexibilidade e simplificar o uso do nosso sistema: **Decorator** e **Facade**.

O **Decorator** é usado para adicionar novos comportamentos a objetos dinamicamente, "envolvendo-os" em objetos decoradores especiais. Isto por que buscamos uma forma 
forma de adicionar elementos extras aos nossos produtos, como "Embrulho para Presente" ou "Estampa Personalizada", sem precisar criar uma subclasse para cada combinação possível (ex: `BrinquedoComEmbrulho`, `BrinquedoComEstampa`, `BrinquedoComAmbos`, etc.). 

**Como foi implementado?**
1.  Criamos uma classe `ProductDecorator` abstrata que herda de `Product`.
2.  Implementamos decorators concretos como `GiftWrapDecorator`, que envolvem um `Product` e modificam seu preço e descrição.

### Padrão Facade

Já o Facade (Fachada) foi usado para termos uma interface unificada e simplificada, escondendo a complexidade do sistema e fornecendo um ponto de entrada mais fácil de usar. Como o processo de criar um produto envolvia conhecer a fábrica correta e, depois, aplicar manualmente os decoradores. Isso ficava muito complexo  na hora de implementar o sistema (cliente). A `StoreFacade` simplifica tudo isso em uma única chamada de método.

**Como foi implementado?**
Criamos a classe `StoreFacade`, que contém a lógica para:
1.  Selecionar a fábrica correta com base em uma string (`'brinquedo'`, `'utilidade'`).
2.  Criar o produto base.
3.  Aplicar os decoradores solicitados através de parâmetros opcionais.
4.  Retornar o produto finalizado para o cliente.

**Exemplo de uso (facade e decorator):**
```python
# O Facade esconde a complexidade de qual fábrica usar.
print("--- Projeto 2 ---")
print("--- Comprando produtos via Facade ---")

# instância da facade da loja
loja = StoreFacade()

# Usando a facade para comprar diferentes tipos de produtos
# Comprando um material escolar
caderno = loja.buy_product(
    product_type='material_escolar',
    name='Caderno Espiral',
    price=25.50
)
# Saída: Compra finalizada: Material Escolar: Caderno Espiral, Preço: R$25.50

# Comprando um brinquedo
carrinho = loja.buy_product(
    product_type='brinquedo',
    name='Carrinho de Polícia',
    price=80.00
)
# Saida: Compra finalizada: Brinquedo: Carrinho de Polícia, Preço: R$80.00

print("\n--- Comprando produto com decoração via Facade ---")

# Comprando um produto e solicitar extras (que usarão os Decorators)
carrinho_final = loja.buy_product(
    product_type='brinquedo',
    name='Carrinho de Controle Remoto',
    price=150.00,
    add_gift_wrap=True,
    custom_stamp="Para o campeão!"
)
# O Facade já retorna o produto final, decorado e com o preço correto.
# Preço final será 150.00 (base) + 10.00 (embrulho) + 5.50 (estampa) = 165.50
```

------------------------------------

# Projeto Atacado Bom Preco - Padrões de Projeto - Projeto 1

Foi escolhido o padrão de projeto Factory Method, com o objetivo de termos uma base uma base sólida para a criação de objetos. O tema aplicado foi da minha loja de produtos, Atacado Bom Preço, desenvolvido com a linguagem Python.

### Por que usar o Factory Method?

O Factory Method foi escolhido por três suas características de extensibilidade, desacoplamento e centralização da lógica de criação. Assim, podemos adicionar novos tipos de produtos sem alterar o código que utiliza os objetos (cliente). Ou seja, supondo que vamos adicionar uma nova categoria de produtos como eletrônicos, precisamos apenas criar a classe `Electronic` e sua respectiva fábrica `ElectronicFactory`. O código que consome as fábricas não precisa ser modificado, pois ele depende da abstração (`ProductFactory`) e não da implementação concreta. Possibilitando um baixo acoplamento entre o código que precisa de um produto (código cliente) e as classes concretas dos produtos. Ou seja, o código cliente interage com a interface da fábrica e com a interface do produto, sem precisar saber qual classe específica está sendo instanciada, o que torna o sistema mais flexível.

Por fim, a centralização da lógica para a criação de cada tipo de produto fica encapsulada em sua própria fábrica. Isso organiza o código e torna a criação de objetos mais explícita e fácil de gerenciar, em vez de espalhar `if/else` ou `switch/case` pelo sistema para decidir qual classe instanciar.

### Como foi Implementado?

A implementação segue a estrutura clássica do padrão:

**1. Abstração do Produto (`Product`)**:
Uma classe base abstrata que define a interface comum para todos os produtos.

```python
# src/interfaces/product.py
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self) -> str:
        pass
```

**2. Produtos Concretos (`SchoolSupply`, `Toy`, `Utility`)**:
Classes que herdam de `Product` e implementam seus próprios detalhes.

```python
# src/products/toy.py
from src.interfaces import Product

class Toy(Product):
    """Representa um produto do tipo Brinquedo."""
    def get_details(self) -> str:
        return f"Brinquedo: {self.name}, Preço: R${self.price:.2f}"
```

**3. Abstração da Fábrica (`ProductFactory`)**:
A classe "Creator" abstrata. Ela possui o `factory_method` que será implementado pelas subclasses.

```python
# src/interfaces/product_factory.py
from abc import ABC, abstractmethod
from .product import Product

class ProductFactory(ABC):
    @abstractmethod
    def factory_method(self, name: str, price: float) -> Product:
        pass

    def create_product(self, name: str, price: float) -> Product:
        product = self.factory_method(name, price)
        return product
```

**4. Fábricas Concretas (`SchoolSupplyFactory`, `ToyFactory`, etc.)**:
Cada fábrica é responsável por instanciar um tipo de produto concreto.

```python
# src/factories/toy_factory.py
from src.interfaces import ProductFactory, Product
from src.products.toy import Toy

class ToyFactory(ProductFactory):
    def factory_method(self, name: str, price: float) -> Product:
        return Toy(name, price)
```

**Exemplo de Uso - Cliente:**

O código cliente decide qual fábrica usar, mas o restante da lógica pode tratar todos os produtos da mesma forma, devido a interface comum.

```python
from src.factories import SchoolSupplyFactory
from src.factories import ToyFactory

# Cliente decide criar material escolar
school_factory = SchoolSupplyFactory()
caderno = school_factory.create_product("Caderno Espiral", 25.50)
print(caderno.get_details())  # Saída: Material Escolar: Caderno Espiral, Preço: R$25.50

# Cliente decide criar um brinquedo
toy_factory = ToyFactory()
carrinho = toy_factory.create_product("Carrinho de Polícia", 80.00)
print(carrinho.get_details())  # Saída: Brinquedo: Carrinho de Polícia, Preço: R$80.00
```

Assim, com essa base e o padrao Factory Method, é possível evoluir e adicionar novos produtos, criar novas funcionalidades, etc, sem comprometer a estrutura existente.
