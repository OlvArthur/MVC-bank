from abc import ABC, abstractmethod
from typing import TypedDict

class Statement(TypedDict):
    name: str
    balance: float


class ClientRepositoryInterface(ABC):

    @abstractmethod
    def withdraw(self, person_name: str, amount: int, amount_limit: int) -> str: pass



    @abstractmethod
    def view_statement(self, person_name: str) -> Statement: pass
