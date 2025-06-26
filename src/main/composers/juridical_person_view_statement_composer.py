from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.juridical_person_repository import JuridicalPersonRepository
from src.controllers.juridical_person_view_statement_controller import (
    JuridicalPersonViewStatementController
)
from src.views.juridical_person_view_statement_view import JuridicalPersonViewStatementView

def juridical_person_view_statement_composer():
    model = JuridicalPersonRepository(db_connection_handler)
    controller = JuridicalPersonViewStatementController(model)
    view = JuridicalPersonViewStatementView(controller)

    return view
