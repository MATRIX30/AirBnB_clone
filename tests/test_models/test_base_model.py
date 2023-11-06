#!/usr/bin/python3
"""
Test module for base model 
"""


import unittest
from models.base_model import BaseModel
import datetime
from io import StringIO
from unittest.mock import patch

class TestBaseModel(unittest.TestCase):
    """ Test class for base model"""
    def test_id(self):
        """Test cases for public instance id attribute"""
        # assert the id is of str type
        self.assertIsInstance(BaseModel().id, str)
        
        # assert two objects won't have same id
        self.assertNotEqual(BaseModel().id, BaseModel().id)

        
        # test if when an object is created both created_at and update_at are same
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)
    
    def test__str__(self):
        """Test __str__ return value"""
        base = BaseModel()
        # testing if __str__ prints correctly
        res = "[{:s}] ({:s}) {}\n".format(base.__class__.__name__, base.id, base.__dict__)
        with patch("sys.stdout", new=StringIO()) as str_out:
            print(base)
            self.assertEqual(str_out.getvalue(), res)