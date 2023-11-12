#!/usr/bin/python3
"""Test Module for file storage"""


import unittest
import json
import os
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class for filestorage"""

    pass

if __name__ == "__main__":
    unittest.main()
