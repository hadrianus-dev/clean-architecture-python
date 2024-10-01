from abc import ABC, abstractmethod
from src.presentation.http.http_request import HttpRequest
from src.presentation.http.http_response import HttpResponse

class ControllerInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: raise NotImplementedError
