from abc import ABC, abstractmethod
from src.models.interfaces.entities.juridical_person import JuridicalPersonInterface

class JuridicalPersonRepositoryInterface(ABC):
    @abstractmethod
    def create(self,
                revenue: float,
                age: int,
                trade_name: str,
                mobile: str,
                corporate_email: str,
                category: str,
                balance: float
              ) -> JuridicalPersonInterface: pass

    @abstractmethod
    def list(self) -> list[JuridicalPersonInterface]: pass
