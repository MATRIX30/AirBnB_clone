#!/usr/bin/python3
"""
Test module for state model
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Test class for users"""

    def test_init(self):
        state1 = State()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(state1, State)
        # test datatype for all attributes
        state1.name = "Bamenda"
        self.assertIsInstance(state1.name, str)

        # test for unique id's for users
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)
        # test for different creation time
        self.assertNotEqual(s1.created_at, s2.created_at)

        # test for different update time
        self.assertNotEqual(s1.updated_at, s2.updated_at)

        # testing default attributes values for user
        self.assertEqual(s1.name, "")

        # test setting attributes
        s1.name = "Bamenda"
        self.assertEqual(s1.name, "Bamenda")

        # test if user attribute can be created from kwarg
        s1 = State(country="Cameroon")
        self.assertEqual(s1.country, "Cameroon")


if __name__ == "__main__":
    unittest.main()
