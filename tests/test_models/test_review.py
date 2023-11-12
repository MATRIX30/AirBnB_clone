#!/usr/bin/python3
"""
Test module for review model
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test class for review"""

    pass

    def test_init(self):
        review1 = Review()
        # test if the object is an instance of the class
        # and not parent class BaseModel
        self.assertIsInstance(review1, Review)
        # test datatype for all attributes
        review1.place_id = "Tekoh"
        self.assertIsInstance(review1.place_id, str)
        review1.user_id = "Palma"
        self.assertIsInstance(review1.user_id, str)
        review1.text = "airbnb@mail.com"
        self.assertIsInstance(review1.text, str)

        # test for unique id's for users
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)
        # test for different creation time
        self.assertNotEqual(r1.created_at, r2.created_at)

        # test for different update time
        self.assertNotEqual(r1.updated_at, r2.updated_at)

        # testing default attributes values for user
        self.assertEqual(r1.text, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.place_id, "")

        # test setting attributes
        r1.text = "its an amazing place i loved it"
        self.assertEqual(r1.text, "its an amazing place i loved it")

        # test if user attribute can be created from kwarg
        r1 = Review(sentiment="Happy")
        self.assertEqual(r1.sentiment, "Happy")

    def test_save(self):
        # testing if save method works for user class
        r3 = Review()
        b = BaseModel()
        self.assertTrue(r3)


if __name__ == "__main__":
    unittest.main()
