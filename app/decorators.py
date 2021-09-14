from flask import request
from functools import wraps

from app.utils import get_json_request
from app.serializer_validators import SerializerValidators


def validate_data(schema):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = get_json_request()
            validator = SerializerValidators(schema, purge_unknown=True)

            if not validator.validate(data):
                return {"errors": validator.errors}, 422

            request.data = validator.normalized(data)

            return func(*args, **kwargs)

        return wrapper
    return inner_function
