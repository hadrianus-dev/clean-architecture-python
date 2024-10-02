
class HttpNotFoundError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.name = "NotFound"
        self.status_code = 404
