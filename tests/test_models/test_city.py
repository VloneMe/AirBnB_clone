#!/usr/bin/python3

"""
Unit tests for the City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test suite for the City class.
    """

    def test_attributes(self):
        """
        Test the initialization of City attributes.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
