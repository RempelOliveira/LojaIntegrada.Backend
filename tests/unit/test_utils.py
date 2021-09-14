import unittest

from tests.main import app
from app.utils import merge_attrs, get_json_request


class TestUtils(unittest.TestCase):
    def test_merge_attrs(self):
        data = {
            "params": {
                "param_one": 1
            }
        }

        merge_data = {
            "params": {
                "param_two": 2
            }
        }

        assert merge_attrs(data, merge_data) == {
            "params": {
                "param_one": 1, "param_two": 2
            }
        }

    def test_get_json_request(self):
        data = {
            "param_one": 123,
            "param_two": 123.5,
            "param_three": "value",
            "param_four": ["value", "value"],
            "param_five": {"param_two": True}
        }

        with app.test_request_context("", data=data):
            assert get_json_request() is not None

        with app.test_request_context("", data=data, content_type="application/json"):
            assert get_json_request() is not None
