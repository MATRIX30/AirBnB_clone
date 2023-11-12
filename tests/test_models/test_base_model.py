#!/usr/bin/python3
"""Test module for base model"""
import unittest
import datetime
from models.base_model import BaseModel
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""

    def test_id(self):
        """Test cases for public instance id attribute"""
        # assert the id is of str type
        self.assertIsInstance(BaseModel().id, str)

        # assert two objects won't have same id
        self.assertNotEqual(BaseModel().id, BaseModel().id)

        # test if when an object is created both created_at and update_at are
        # not more than 2 secs apart
        base = BaseModel()
        self.assertAlmostEqual(
            base.created_at, base.updated_at, delta=datetime.timedelta(
                seconds=2)
        )

    def test__str__(self):
        """Test __str__ return value"""
        base = BaseModel()
        # testing if __str__ prints correctly
        res = "[{:s}] ({:s}) {}\n".format(
            base.__class__.__name__, base.id, base.__dict__
        )
        with patch("sys.stdout", new=StringIO()) as str_out:
            print(base)
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dict(self):
        """Test for to_dic method"""
        base = BaseModel()
        dic = base.to_dict()
        # assert method returns dictionary
        self.assertIsInstance(dic, dict)
        # assert creat_at and update_at are all strings
        self.assertIsInstance(dic["created_at"], str)
        self.assertIsInstance(dic["updated_at"], str)

        # assert the dic has a key called __class__  having the class name
        self.assertEqual(dic["__class__"], base.__class__.__name__)

        # testing if __class__ key exist in dic

    def test_create_baseModel_from_dict(self):
        """Testing creation of base model from dict datastructure"""
        pass


if __name__ == "__main__":
    unittest.main()
