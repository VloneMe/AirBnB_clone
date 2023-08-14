#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test suite for the FileStorage class.
    """
    def setUp(self):
        """
        Set up a fresh instance of FileStorage for each test method.
        """
        self.storage = FileStorage()

    def test_new_and_all(self):
        """
        Test the new and all methods of FileStorage.
        """
        model = BaseModel()
        self.storage.new(model)
        all_objects = self.storage.all()
        self.assertIn(f'BaseModel.{model.id}', all_objects)
        self.assertEqual(all_objects[f'BaseModel.{model.id}'], model)


if __name__ == '__main__':
    unittest.main()
