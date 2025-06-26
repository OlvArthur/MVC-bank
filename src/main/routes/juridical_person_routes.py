from flask import Blueprint,  jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composers.juridical_person_view_statement_composer import (
    juridical_person_view_statement_composer
)

juridical_person_routes_bp = Blueprint('juridical_person_routes', __name__)

@juridical_person_routes_bp.route('/juridical/view-statement/<person_name>', methods=['GET'])
def view_statement(person_name):
    try:
        http_request = HttpRequest(params={'name': person_name})
        view = juridical_person_view_statement_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exc:
        raise exc
