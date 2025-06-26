from src.models.interfaces.entities.juridical_person import JuridicalPersonInterface
from src.models.sqlite.entities.juridical_person import JuridicalPersonTable

def test_entity_interface_implementation():
    assert isinstance(JuridicalPersonTable(),JuridicalPersonInterface)
