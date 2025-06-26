from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.interfaces.entities.natural_person import NaturalPersonInterface

def test_entity_interface_implementation():
    assert isinstance(NaturalPersonTable(), NaturalPersonInterface)
