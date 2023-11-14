#!/usr/bin/python3
"""Test module for base model"""
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from io import StringIO
import json
import os
import models
from unittest.mock import patch
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test class for base model"""

    def test_init(self):
        # test if when an object is created both created_at and update_at are
        # not more than 2 secs apart
        base = BaseModel()
        self.assertAlmostEqual(
            base.created_at, base.updated_at,
            delta=datetime.timedelta(seconds=2)
        )

        # testing if 2 base objects should not have same id
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2)

        # test if updated_at attribute changes when object is saved
        old_date = b1.updated_at
        b1.save()
        new_date = b1.updated_at
        self.assertNotEqual(old_date, new_date)

    def test_id(self):
        """Test cases for public instance id attribute"""
        # assert the id is of str type
        self.assertIsInstance(BaseModel().id, str)

        # assert two objects won't have same id
        self.assertNotEqual(BaseModel().id, BaseModel().id)

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

        # test if to_dict has all attributes like self.__dict__
        dic1 = base.to_dict()
        dic2 = base.__dict__
        dic2["created_at"] = dic2["created_at"].isoformat()
        dic2["updated_at"] = dic2["updated_at"].isoformat()
        dic2["__class__"] = "BaseModel"
        self.assertDictEqual(dic2, dic1)

    def test_create_baseModel_from_dict(self):
        """Testing creation of base model from dict datastructure"""
        pass

    def test_save(self):
        """Testing if save method works"""
        b = BaseModel()
        b_dic = b.to_dict()
        b_json = json.dumps(b_dic)
        file_obj = StringIO()
        file_obj.write(b_json)
        models.storage.new(b)
        models.storage.save()

        # Save the in-memory file obj(file_obj) to disk
        with open("tmp.json", "w") as f:
            f.write(file_obj.getvalue())

        # test if the file file_json exist after writing
        self.assertTrue(os.path.exists("tmp.json"))

        # test if file is not empty
        file_size = os.path.getsize("tmp.json")
        self.assertGreater(file_size, 0)

    def test_base_save(self):
        # test update attribute if it changes after save
        b = BaseModel()
        first_update = b.updated_at
        sleep(1)
        b.save()
        self.assertLess(first_update, b.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
