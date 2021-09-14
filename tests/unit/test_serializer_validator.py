import uuid
import unittest

from app.serializer_validators import SerializerValidators


class TestSerializerValidators(unittest.TestCase):
    validators = SerializerValidators()

    def test__validate_instance_of_uuid(self):
        assert not self.validators._validate_instance_of_uuid(
            None, "uuid", uuid.uuid4())

        with self.assertRaises(Exception):
            self.validators._validate_instance_of_uuid(None, "uuid", "value")
