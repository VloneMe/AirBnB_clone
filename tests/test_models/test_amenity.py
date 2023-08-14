#!/usr/bin/python3

"""
Unit tests for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class.
    """

    def test_attributes(self):
        """
        Test the initialization of Amenity attributes.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
