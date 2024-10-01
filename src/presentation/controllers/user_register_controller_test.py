# pylint: disable=C0301
from src.presentation.controllers.user_register_controller import UserRegisterController
from src.presentation.http.http_request import HttpRequest
from src.presentation.http.http_response import HttpResponse
from src.data.tests.user_register import UserRegisterSpy


def test_handle():
    http_request = HttpRequest(body={'first_name': 'John', 'last_name': 'Doe', 'age': 30})
    use_case = UserRegisterSpy()
    controller = UserRegisterController(use_case)
    response = controller.handle(http_request)
    print()

    assert response.status_code == 202
    assert isinstance(response, HttpResponse)
    assert response.body is not None
    assert response.body == {'data': {'type': 'User', 'count': 1, 'attributes': [{'first_name': 'John', 'last_name': 'Doe', 'age': 30}]}}
