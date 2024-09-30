from typing import Dict
from src.infra.db.repositories.users_repository import UserRepository
from .user_finder import UserFinder

class TestFinder:

    def find(self, first_name: str) -> Dict:
        repository = UserRepository()
        user_finder = UserFinder(repository)
        return user_finder.find(first_name)
