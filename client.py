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
