from src.factories import SchoolSupplyFactory
from src.factories import ToyFactory
from src.products.toy import Toy
from src.facade import StoreFacade


print("--- Projeto 1 ---")
print("--- Comprando produtos via Factory ---")

# Cliente decide criar material escolar
school_factory = SchoolSupplyFactory()
caderno = school_factory.create_product("Caderno Espiral", 25.50)
print(caderno.get_details())  # Saída: Material Escolar: Caderno Espiral, Preço: R$25.50

# Cliente decide criar um brinquedo
toy_factory = ToyFactory()
carrinho = toy_factory.create_product("Carrinho de Polícia", 80.00)
print(carrinho.get_details())  # Saída: Brinquedo: Carrinho de Polícia, Preço: R$80.00



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
# Nao precisa do print
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