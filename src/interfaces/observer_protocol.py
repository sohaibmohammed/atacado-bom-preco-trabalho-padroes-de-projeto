from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

# Forward reference para o Subject
class Subject(ABC):
    """A interface do Subject (ou 'Observable')."""
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Anexa um observador ao subject."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Desanexa um observador."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notifica todos os observadores sobre um evento."""
        pass

class Observer(ABC):
    """A interface do Observer."""
    @abstractmethod
    def update(self, data: Any) -> None:
        """Recebe a atualização do subject."""
        pass