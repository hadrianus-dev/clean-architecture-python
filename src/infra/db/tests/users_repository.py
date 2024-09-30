from typing import List
from src.domain.models.users import Users

class UserRepositorySpy:

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}
        self.insert_user_result = None
        self.select_user_result = None

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_params = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_params = {"first_name": first_name}
        return [
            Users(1, first_name, last_name="Doe", age=30),
            Users(2, first_name, last_name="Doe2", age=25),
            Users(3, first_name, last_name="Doe3", age=20),
            Users(4, first_name, last_name="Doe4", age=15),
        ]
