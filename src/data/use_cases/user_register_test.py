from src.infra.db.tests.users_repository import UserRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = "MyNameIsJohn"
    last_name = "Doe"
    age = 30

    repository = UserRepositorySpy()
    user_register = UserRegister(repository)

    response = user_register.register(first_name, last_name, age)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["attributes"] == {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

    assert repository.insert_user_params["first_name"] == first_name
    assert repository.insert_user_params["last_name"] == last_name
    assert repository.insert_user_params["age"] == age


def test_register_first_name_error():
    first_name = "MyNameIsJohn213"
    last_name = "Doe"
    age = 30

    repository = UserRepositorySpy()
    user_register = UserRegister(repository)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as e:
        assert str(e) == "The first name must be only letters"
