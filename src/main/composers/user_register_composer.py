from src.infra.db.repositories.users_repository import UserRepository
from src.data.use_cases.user_register import UserRegister as UserRegisterUseCase
from src.presentation.controllers.user_register_controller import UserRegisterController

def user_register_composer():
    users_repository = UserRepository()
    user_register_use_case = UserRegisterUseCase(users_repository)
    user_register_controller = UserRegisterController(user_register_use_case)
    return user_register_controller.handle
