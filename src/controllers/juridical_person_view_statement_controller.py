from src.models.interfaces.repositories.client import ClientRepositoryInterface, Statement

class JuridicalPersonViewStatementController:
    def __init__(self, juridical_person_repository: ClientRepositoryInterface) -> None:
        self.__repository = juridical_person_repository

    def execute(self, person_name: str) -> Statement:
        try:
            statement = self.__repository.view_statement(person_name)

            return statement

        except Exception as exc:
            raise exc
