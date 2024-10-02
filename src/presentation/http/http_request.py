# pylint: disable=R0913
# pylint: disable=R0917
class HttpRequest:
    def __init__(
            self,
            headers: dict = None,
            body: dict = None,
            query_params: dict = None,
            path_params: dict = None,
            url: str = None,
            ipv4: str = None
        ):
        self.headers = headers if headers is not None else {
            'Acept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
