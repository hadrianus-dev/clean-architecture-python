# pylint: disable=E0611
# pylint: disable=C0301
from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy
from src.presentation.http.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self):
        self.query_params = { 'first_name': 'John' }


def test_handle():
    http_request = HttpRequestMock()
    use_case = UserFinderSpy()
    controller = UserFinderController(use_case)
    response = controller.handle(http_request)
    print()

    assert isinstance(response, HttpResponse)
    assert response.body is not None
    assert response.status_code == 200
    assert response.body == {'data': {'type': 'User', 'count': 1, 'attributes': [{'first_name': 'John', 'last_name': 'Doe', 'age': 30}]}}
