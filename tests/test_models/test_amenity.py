#!/usr/bin/python3
"""
Test module for amenity model
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test class for amenity"""

    def test_init(self):
        amenity1 = Amenity()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(amenity1, Amenity)
        # test datatype for all attributes
        amenity1.name = "Hilux_vehicle"
        self.assertIsInstance(amenity1.name, str)

        # test for unique id's for users
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)
        # test for different creation time
        self.assertNotEqual(a1.created_at, a2.created_at)

        # test for different update time
        self.assertNotEqual(a1.updated_at, a2.updated_at)

        # testing default attributes values for user
        self.assertEqual(a1.name, "")

        # test setting attributes
        a1.name = "Hilux_vehicle"
        self.assertEqual(a1.name, "Hilux_vehicle")

        # test if user attribute can be created from kwarg
        a1 = Amenity(price=20000)
        self.assertEqual(a1.price, 20000)


if __name__ == "__main__":
    unittest.main()
