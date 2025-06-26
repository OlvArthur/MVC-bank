import pytest
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.natural_person import NaturalPersonTable

db_connection_handler.connect_to_db()

@pytest.mark.skip('Database interaction')
def test_list_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)

    people = repo.list()

    print(people)
    assert len(people) != 0


@pytest.mark.skip('Database interaction')
def test_create():
    repo = NaturalPersonRepository(db_connection_handler)

    natural_person = repo.create(
        age=32,
        balance=20000,
        category='B',
        email='john@doe.com',
        full_name='John Doe',
        mobile='12344',
        monthly_income=1200
    )

    assert isinstance(natural_person, NaturalPersonTable)
