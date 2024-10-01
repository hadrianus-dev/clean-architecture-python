
class UserRegisterSpy:
    def __init__(self) -> None:
        self.register_attribute = {}

    def register(self, first_name: str, last_name: str, age: int) -> dict:
        self.register_attribute['first_name'] = first_name
        self.register_attribute['last_name'] = last_name
        self.register_attribute['age'] = age

        return {
            "type": "User",
            "count": 1,
            "attributes": [
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": age
                }
            ]
        }
