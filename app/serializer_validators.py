from uuid import UUID
from cerberus import Validator


class SerializerValidators(Validator):
    def _validate_instance_of_uuid(self, constraint, field, value):
        "{'type': 'boolean'}"

        try:
            UUID(str(value))
        except ValueError:
            self._error(field, "Must be a uuid string")
