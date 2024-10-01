from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http.http_request import HttpRequest
from src.presentation.http.http_response import HttpResponse

class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            query = http_request.query_params["first_name"]
            response = self.__use_case.find(query)
            return HttpResponse(status_code=200, body={'data': response})
        except Exception as e:
            return HttpResponse(status_code=500, body={'error message': str(e)})
