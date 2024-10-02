from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_register_validator(request: any):
    body_validator = Validator({
        "first_name": {
            "required": True,
            "type": "string",
            "empty": False,
            "maxlength": 18
        },
        "last_name": {
            "required": True,
            "type": "string",
            "empty": False,
            "maxlength": 18
        },
        "age": {
            "required": True,
            "type": "integer",     
            "empty": False 
        }
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
