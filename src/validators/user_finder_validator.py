from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_finder_validator(request: any):
    query_validator = Validator({
        "first_name": {
            "required": True,
            "type": "string",
            "empty": False,
            "maxlength": 18
        },
    })

    response = query_validator.validate(request.args)
    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
