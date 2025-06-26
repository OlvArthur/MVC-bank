from src.models.interfaces.repositories.client import ClientRepositoryInterface

class JuridicalPersonWithdrawController:
    def __init__(self, juridical_person_repository: ClientRepositoryInterface) -> None:
        self.__repository = juridical_person_repository
        self.__withdraw_limit = 12000

    def execute(self,person_name: str, amount: float ) -> str:
        try:
            message = self.__repository.withdraw(
                person_name=person_name,
                amount=amount,
                amount_limit=self.__withdraw_limit
            )

            return message

        except Exception as exc:
            raise exc
