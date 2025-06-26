from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.interfaces.repositories.natural_person_repository import (
   NaturalPersonRepositoryInterface
)
from src.models.interfaces.repositories.client import ClientRepositoryInterface, Statement
from src.models.interfaces.entities.natural_person import NaturalPersonInterface
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepository(NaturalPersonRepositoryInterface, ClientRepositoryInterface):
    def __init__(self, db_connection_handler: DBConnectionHandler) -> None:
        self.__db_connection_handler = db_connection_handler

    def view_statement(self, person_name) -> Statement:
        with self.__db_connection_handler as database:
            try:
                person = (
                     database.session
                            .query(NaturalPersonTable)
                            .filter_by(name=person_name)
                            .first()
                 )

                return {
                     'name': person_name,
                     'balance': person.balance
                 }

            except Exception as exc:
                raise exc

    def withdraw(self, person_name: str, amount: int, amount_limit: int) -> str:
        if amount > amount_limit:
            raise Exception('amount not allowed')

        with self.__db_connection_handler as database:
            try:
                person = (
                    database.session
                        .query(NaturalPersonTable)
                        .filter_by(name=person_name)
                        .first()
                )

                if person is None:
                    raise Exception('Person not found')

                if amount > person.balance:
                    raise Exception('Amount not available')

                person.balance -= amount
                database.session.commit()

                return f'Withdraw of ${amount} successfully completed'
            except Exception as exc:
                database.session.rollback()
                raise exc


    def list(self) -> list[NaturalPersonInterface]:
        with self.__db_connection_handler as database:
            people = database.session.query(NaturalPersonTable).all()
            return people

    def create(self, monthly_income, age, full_name, mobile, email, category, balance):
        with self.__db_connection_handler as database:
            try:
                new_person = NaturalPersonTable(
                    monthly_income=monthly_income,
                    age=age,
                    full_name=full_name,
                    mobile=mobile,
                    email=email,
                    category=category,
                    balance=balance
                )
                database.session.add(new_person)
                database.session.commit()
                return new_person
            except Exception as exc:
                database.session.rollback()
                raise exc
