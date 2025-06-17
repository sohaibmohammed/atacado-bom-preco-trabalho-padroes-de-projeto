# Imports para a demonstração da Fase 1 (Uso direto da Factory)
from src.factories import SchoolSupplyFactory
from src.factories import ToyFactory

# Import para a Facade (usada a partir da Fase 2)
from src.facade import StoreFacade

# Imports para a Fase 3 (Padrões Comportamentais)
from src.strategies import CreditCardPaymentStrategy, PixPaymentStrategy
from src.observers import InventoryObserver, EmailObserver


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
print("\n--- Projeto 2 ---")
print("--- Comprando produtos via Facade ---")

# instância da facade da loja
loja = StoreFacade()

# AJUSTE: O método buy_product agora exige uma estratégia de pagamento.
# Vamos definir uma estratégia padrão para que estes exemplos da Fase 2 continuem funcionando.
estrategia_padrao_cartao = CreditCardPaymentStrategy()


# Usando a facade para comprar diferentes tipos de produtos
# Comprando um material escolar
loja.buy_product(
    product_type='material_escolar',
    name='Caderno Espiral',
    price=25.50,
    payment_strategy=estrategia_padrao_cartao # Argumento adicionado para compatibilidade
)
# A Facade agora imprime os detalhes da compra, então o print aqui não é mais necessário.

# Comprando um brinquedo
loja.buy_product(
    product_type='brinquedo',
    name='Carrinho de Polícia',
    price=80.00,
    payment_strategy=estrategia_padrao_cartao # Argumento adicionado para compatibilidade
)

print("\n--- Comprando produto com decoração via Facade ---")

# Comprando um produto e solicitar extras (que usarão os Decorators)
loja.buy_product(
    product_type='brinquedo',
    name='Carrinho de Controle Remoto',
    price=150.00,
    payment_strategy=estrategia_padrao_cartao, # Argumento adicionado para compatibilidade
    add_gift_wrap=True,
    custom_stamp="Para o campeão!"
)
# O Facade já retorna o produto final, decorado e com o preço correto.


print("\n--- Projeto 3 ---")
print("--- Demonstrando Padrões Comportamentais (Strategy e Observer) ---")

# A facade já foi instanciada na seção do Projeto 2, vamos reutilizá-la.
# 1. Anexando os observadores (Padrão Observer)
print("\nAnexando observadores ao sistema...")
loja.attach(InventoryObserver())
loja.attach(EmailObserver())

# 2. Criando uma nova estratégia de pagamento para a demonstração (Padrão Strategy)
estrategia_pix = PixPaymentStrategy()

# 3. Realizando uma compra que acionará todos os padrões
print("\n--- Realizando compra completa com Pix, decoração e observadores ---")
loja.buy_product(
    product_type='material_escolar',
    name='Mochila Personalizada',
    price=180.00,
    payment_strategy=estrategia_pix, # Usando a nova estratégia de Pix
    add_gift_wrap=True,
    custom_stamp="Ano Letivo 2025"
)