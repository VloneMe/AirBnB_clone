#!/usr/bin/python3

"""
Unit tests for the State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def test_attributes(self):
        """
        Test the initialization of State attributes.
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
