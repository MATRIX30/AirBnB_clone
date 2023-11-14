#!/usr/bin/python3
"""Test module for file_storage"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class for file_storage"""

    def setUp(self):
        """rename our main file_json file before running test"""
        try:
            os.rename("file_json", "tmp")

        except Exception:
            pass

    def tearDown(self):
        try:
            os.remove("file_obj")
            os.rename("tmp", "file_json")
        except Exception:
            pass

    def test_file_obj(self):
        """Test for file object"""
        storage = FileStorage()
        # test if attribute is private
        self.assertEqual(type(FileStorage()), FileStorage)
        with self.assertRaises(AttributeError):
            FileStorage.__file_path

    def test_file_file_path(self):
        """Test for file_path"""
        pass

    def test_save(self):
        """Test for save  method"""
        base = BaseModel()
        # assert the method save exist
        self.assertIn("save", FileStorage.__dict__)

    def test_all(self):
        """Test for all method"""
        # test if it returns dictionary object
        storage = FileStorage()
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """Test for save method"""
        base = BaseModel()
        user = User()
        storage = FileStorage()
        storage.new(base)
        storage.new(user)
        
        self.assertIn("BaseModel." + base.id, storage.all().keys())

    def test_reload(self):
        """Test for reload method"""
        # assert the method save exist
        self.assertIn("reload", FileStorage.__dict__)


if __name__ == "__main__":
    unittest.main()
