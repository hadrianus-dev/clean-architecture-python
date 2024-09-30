from typing import Dict
from src.infra.db.tests.users_repository import UserRepositorySpy
from .user_finder import UserFinder

class TestFinder:

    def test_find(self, first_name="MyNameIsJohn") -> Dict:
        repository = UserRepositorySpy()
        user_finder = UserFinder(repository)
        response = user_finder.find(first_name)

        assert response["type"] == "User"
        assert response["count"] == len(response["attributes"])
        assert response["attributes"] != [] # pylint: disable=C1803

    def test_find_error_in_valid_name(self):
        repository = UserRepositorySpy()
        user_finder = UserFinder(repository)

        try:
            user_finder.find("123")
            assert False
        except Exception as e:
            assert str(e) == "The first name must be only letters"


    def test_find_error_in_too_long_name(self):
        repository = UserRepositorySpy()
        user_finder = UserFinder(repository)

        try:
            user_finder.find("NabucodonozorNinrodenren")
            assert False
        except Exception as e:
            assert str(e) == "The first name must be less than 18 characters"


    def test_find_error_in_user_not_found(self):
        class UserRepositoryError(UserRepositorySpy):
            def select_user(self, first_name: str):
                return []

        first_name = "MyNameIsJohn"

        repository = UserRepositoryError()
        user_finder = UserFinder(repository)

        try:
            user_finder.find(first_name)
            assert False
        except Exception as e:
            assert str(e) == "User not found"
