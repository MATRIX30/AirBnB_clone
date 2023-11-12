#!/usr/bin/python3
"""
Test module for place model
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test class for place"""

    def test_init(self):
        place1 = Place()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(place1, Place)
        # test datatype for all attributes

        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.user_id, str)
        place1.name = "Sadle Hills Bamenda"
        self.assertIsInstance(place1.name, str)
        place1.description = "A grassland resort"
        self.assertIsInstance(place1.description, str)
        place1.number_rooms = 4
        self.assertIsInstance(place1.number_rooms, int)
        place1.number_bathrooms = 1
        self.assertIsInstance(place1.number_bathrooms, int)
        place1.max_guest = 5
        self.assertIsInstance(place1.max_guest, int)
        place1.price_by_night = 10000
        self.assertIsInstance(place1.price_by_night, int)
        place1.latitude = 112.5
        self.assertIsInstance(place1.latitude, float)
        place1.longitude = 5.25
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.amenity_ids, list)

        # test for unique id's for users
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)
        # test for different creation time
        self.assertNotEqual(p1.created_at, p2.created_at)

        # test for different update time
        self.assertNotEqual(p1.updated_at, p2.updated_at)

        # testing default attributes values for user
        place1.name = "Sadle Hills Bamenda"
        self.assertIsInstance(place1.name, str)
        place1.description = "A grassland resort"
        self.assertIsInstance(place1.description, str)
        place1.number_rooms = 4
        self.assertIsInstance(place1.number_rooms, int)
        place1.number_bathrooms = 1
        self.assertIsInstance(place1.number_bathrooms, int)
        place1.max_guest = 5
        self.assertIsInstance(place1.max_guest, int)
        place1.price_by_night = 10000
        self.assertIsInstance(place1.price_by_night, int)
        place1.latitude = 1.3
        self.assertIsInstance(place1.latitude, float)
        place1.longitude = 5.25
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.amenity_ids, list)

        self.assertEqual(p1.name, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.latitude, 0.0)
        self.assertEqual(p1.longitude, 0.0)
        self.assertEqual(p1.amenity_ids, [])
