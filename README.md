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