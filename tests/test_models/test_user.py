#!/usr/bin/python3
"""
Test module for state model
"""

import datetime
from io import StringIO
import json
import os
from time import sleep
import unittest
from unittest.mock import patch
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
        
    def test_id(self):
        """Test cases for public instance id attribute"""
        # assert the id is of str type
        self.assertIsInstance(User().id, str)

        # assert two objects won't have same id
        self.assertNotEqual(User().id, User().id)

    def test__str__(self):
        """Test __str__ return value"""
        user = User()
        # testing if __str__ prints correctly
        res = "[{:s}] ({:s}) {}\n".format(
            user.__class__.__name__, user.id, user.__dict__
        )
        with patch("sys.stdout", new=StringIO()) as str_out:
            print(user)
            self.assertEqual(str_out.getvalue(), res)



            # Save the in-memory file obj(file_obj) to disk
    def test_save(self):
        """Testing if save method works"""
        storage = FileStorage()
        b = User()
        b_dic = b.to_dict()
        b_json = json.dumps(b_dic)
        file_obj = StringIO()
        file_obj.write(b_json)
       
        with open("tmp.json", "w") as f:
            f.write(file_obj.getvalue())

        # test if the file file_json exist after writing
        self.assertTrue(os.path.exists("tmp.json"))

        # test if file is not empty
        file_size = os.path.getsize("tmp.json")
        self.assertGreater(file_size, 0)


if __name__ == "__main__":
    unittest.main()
