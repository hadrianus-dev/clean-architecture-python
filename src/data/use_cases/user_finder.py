from typing import Dict, List
from src.domain.models.users import Users
from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_users(first_name)
        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise ValueError("The first name must be only letters")

        if len(first_name) > 18:
            raise ValueError("The first name must be less than 18 characters")

    def __search_users(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if not users: raise Exception("User not found") # pylint: disable=W0719
        return users


    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age
            })

        response = {
            'type': 'User',
            'count': len(users),
            'attributes': attributes
        }

        return response
