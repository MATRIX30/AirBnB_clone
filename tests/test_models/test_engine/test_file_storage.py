#!/usr/bin/python3
"""Test module for file storage class
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test class for file storage"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp_json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_attributes(self):
        self.assertIsInstance(FileStorage.__file_path, str)
        self.assertIsInstance(FileStorage.__objects, dict)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        basemodel = BaseModel()
        models.storage.new(basemodel)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        us = User()
        models.storage.new(us)

        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("User." + us.id, text)

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as file:
            file.write("{}")
        with open("file.json", "r") as reader:
            for line in reader:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_reload(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
