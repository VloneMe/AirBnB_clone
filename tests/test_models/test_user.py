#!/usr/bin/python3

"""
Unit tests for the User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test suite for the User class.
    """

    def test_attributes(self):
        """
        Test the initialization of User attributes.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
