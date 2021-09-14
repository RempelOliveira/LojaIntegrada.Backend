import unittest
from app.constants import DISCOUNT_TYPES


class TestConstants(unittest.TestCase):
    def test_discount_types(self):
        assert type(DISCOUNT_TYPES) == list
