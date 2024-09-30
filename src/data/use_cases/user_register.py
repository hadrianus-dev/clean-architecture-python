# pylint: disable=E0401
# pylint: disable=E0611
from typing import Dict
from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate_name(first_name)
        self.__validate_name(last_name)
        self.__register_user_information(first_name, last_name, age)

        return self.__format_response(first_name, last_name, age)


    def __register_user_information(self, first_name: str, last_name: str, age: int) -> None:
        self.__users_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise ValueError("The first name must be only letters")

        if len(name) > 18:
            raise ValueError("The first name must be less than 18 characters")

    @classmethod
    def __format_response(cls, fist_name: str, last_name: str, age: int) -> Dict:
        response = {
            'type': 'User',
            'count': 1,
            'attributes': {
                'first_name': fist_name,
                'last_name': last_name,
                'age': age
            },
        }

        return response
