from src.infra.db.repositories.users_repository import UserRepository
from src.data.use_cases.user_finder import UserFinder as UserFinderUseCase
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_finder_composer():
    users_repository = UserRepository()
    user_finder_use_case = UserFinderUseCase(users_repository)
    user_finder_controller = UserFinderController(user_finder_use_case)
    return user_finder_controller.handle
