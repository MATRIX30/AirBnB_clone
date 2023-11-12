#!/usr/bin/python3
"""
Test module for city model
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test class for city"""

    def test_init(self):
        city1 = City()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(city1, City)
        # test datatype for all attributes
        city1.name = "Tekoh"
        self.assertIsInstance(city1.name, str)
        city1.id = "Palma"
        self.assertIsInstance(city1.id, str)

        # test for unique id's for users
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)
        # test for different creation time
        self.assertNotEqual(c1.created_at, c2.created_at)

        # test for different update time
        self.assertNotEqual(c1.updated_at, c2.updated_at)

        # testing default attributes values for user

        self.assertNotEqual(c1.id, "")
        self.assertEqual(c1.name, "")

        # test setting attributes
        c1.name = "Tekoh"
        self.assertEqual(c1.name, "Tekoh")

        # test if user attribute can be created from kwarg
        c1 = City(population=200000)
        self.assertEqual(c1.population, 200000)

    def test_save(self):
        # testing if save method works for user class
        c3 = City()
        b = BaseModel()
        self.assertTrue(c3)
