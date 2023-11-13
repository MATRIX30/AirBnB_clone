#!/usr/bin/python3
"""
Test module for state model
"""

import datetime
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test class for users"""

    def test_init(self):
        user1 = User()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(user1, User)
        # test datatype for all attributes
        self.assertIsInstance(user1.id, str)
        user1.first_name = "Bamenda"
        self.assertIsInstance(user1.first_name, str)
        user1.last_name = "Bamenda"
        self.assertIsInstance(user1.last_name, str)
        user1.email = "airbnb@gmail.com"
        self.assertIsInstance(user1.email, str)
        user1.password = "root"
        self.assertIsInstance(user1.password, str)

        # test for unique id's for users
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)
        # test for different creation time
        self.assertNotEqual(u1.created_at, u2.created_at)

        # test for different update time
        self.assertNotEqual(u1.updated_at, u2.updated_at)

        # testing default attributes values for user
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime)
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.password, str)

        # test setting attributes
        u1.password = "hack"
        self.assertEqual(u1.password, "hack")

        # test if user attribute can be created from kwarg
        u1 = User(country="Cameroon")
        self.assertEqual(u1.country, "Cameroon")


if __name__ == "__main__":
    unittest.main()
