from src.models.interfaces.repositories.juridical_person_repository import (
  JuridicalPersonRepositoryInterface
)
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.juridical_person import JuridicalPersonTable
from src.models.interfaces.repositories.client import ClientRepositoryInterface, Statement

class JuridicalPersonRepository(JuridicalPersonRepositoryInterface, ClientRepositoryInterface):
    def __init__(self, db_connection_handler: DBConnectionHandler):
        self.__db_connection_handler = db_connection_handler

    def view_statement(self, person_name) -> Statement:
        with self.__db_connection_handler as database:
            try:
                person = (
                     database.session
                            .query(JuridicalPersonTable)
                            .filter_by(trade_name=person_name)
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
                        .query(JuridicalPersonTable)
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


    def create(self, revenue, age, trade_name, mobile, corporate_email, category, balance):
        with self.__db_connection_handler as database:
            try:
                new_person = JuridicalPersonTable(
                    revenue = revenue,
                    age = age,
                    trade_name = trade_name,
                    mobile = mobile,
                    corporate_email = corporate_email,
                    category = category,
                    balance = balance
                )
                database.session.add(new_person)
                database.session.commit()
                return new_person
            except Exception as exc:
                database.session.rollback()
                raise exc

    def list(self):
        with self.__db_connection_handler as database:
            people = database.session.query(JuridicalPersonTable).all()
            return people
