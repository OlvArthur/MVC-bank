from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class JuridicalPersonViewStatementView:
    def __init__(self, juridical_person_view_statement_controller):
        self.__controller = juridical_person_view_statement_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_name = http_request.params['name']

        statement = self.__controller.execute(person_name)

        return HttpResponse(status_code=200, body=statement)
