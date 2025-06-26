import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.juridical_person import JuridicalPersonTable

from .juridical_person_repository import JuridicalPersonRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip('Database Interaction')
def test_list_juridical_person():
    repo = JuridicalPersonRepository(db_connection_handler)
    people = repo.list()

    print(people)

    assert len(people) != 0


@pytest.mark.skip('Database Interaction')
def test_create_juridical_person():
    repo = JuridicalPersonRepository(db_connection_handler)

    new_person = repo.create(
        revenue=3500,
        age=32,
        trade_name='Lojas',
        mobile='1223245',
        corporate_email='jhon.doe@lojas.com',
        category='Marketing',
        balance=200000
    )

    assert isinstance(new_person, JuridicalPersonTable)
