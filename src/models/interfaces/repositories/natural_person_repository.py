from abc import ABC, abstractmethod
from src.models.interfaces.entities.natural_person import NaturalPersonInterface

class NaturalPersonRepositoryInterface(ABC):

    @abstractmethod
    def create(self,
                monthly_income: float,
                age: int,
                full_name: str,
                mobile: str,
                email: str,
                category: str,
                balance: float
              ) -> NaturalPersonInterface: pass

    @abstractmethod
    def list(self) -> list[NaturalPersonInterface]: pass
