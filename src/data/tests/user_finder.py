
class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attribute = {}

    def find(self, first_name: str) -> dict:
        self.find_attribute['first_name'] = first_name

        return {
            "type": "User",
            "count": 1,
            "attributes": [
                {
                    "first_name": first_name,
                    "last_name": "Doe",
                    "age": 30
                }
            ]
        }
