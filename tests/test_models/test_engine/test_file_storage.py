#!/usr/bin/python3
"""Test module for file_storage"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):
    """Test class for file_storage"""
  
    def setUp(self):
        """rename our main file_json file before running test"""
        try:
            os.rename("file_json", "tmp")
            
        except:
            pass
        
        
    def tearDown(self):
        try:
            os.remove("file_obj")
            os.rename("tmp", "file_json")
        except:
            pass
        
    def test_file_obj(self):
        """ Test for file object"""
        # test if attribute is private
        self.assertEqual(type(FileStorage()), FileStorage)
        
        
    def test_file_file_path(self):
        """ Test for file_paht"""
        pass
    
    def test_save(self):
        """Test for save  method"""
        base = BaseModel()

    
    
    def test_all(self):
        """Test for all method"""
        # test if it returns dictionary object
        storage = FileStorage()
        
        self.assertEqual(dict,type(FileStorage.all(storage)))
    
    def test_new(self):
        """Test for save method"""
        pass
    
    def test_reload(self):
        """Test for reload method"""
        pass


if __name__ == "__main__":
    unittest.main()
