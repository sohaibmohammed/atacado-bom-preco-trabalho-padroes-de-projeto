# src/factories/__init__.py

# Importa as classes dos módulos para o nível do pacote.
# O "." antes do nome do módulo significa "do mesmo pacote".
# Isto corrige erro de importacoes nos testes
from .school_supply_factory import SchoolSupplyFactory
from .toy_factory import ToyFactory
from .utility_factory import UtilityFactory