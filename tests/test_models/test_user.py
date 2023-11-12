#!/usr/bin/python3
"""
Test module for User model
"""

import unittest

from black import assert_equivalent
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test class for User"""

    def test_init(self):
        user1 = User()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(user1, User)
        # test datatype for all attributes
        user1.first_name = "Tekoh"
        self.assertIsInstance(user1.first_name, str)
        user1.last_name = "Palma"
        self.assertIsInstance(user1.last_name, str)
        user1.email = "airbnb@mail.com"
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
        self.assertEqual(u1.email, "")
        self.assertEqual(u1.last_name, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")

        # test setting attributes
        u1.first_name = "Tekoh"
        self.assertEqual(u1.first_name, "Tekoh")
        u1.last_name = "Palma"
        self.assertEqual(u1.last_name, "Palma")
        u1.email = "airbnb@gmail.com"
        self.assertEqual(u1.email, "airbnb@gmail.com")
        u1.password = "root"
        self.assertEqual(u1.password, "root")

        # test if user attribute can be created from kwarg
        u1 = User(age=2)
        self.assertEqual(u1.age, 2)
        # testing if save method works for user class
        # user1.save()
