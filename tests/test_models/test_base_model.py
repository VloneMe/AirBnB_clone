#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a fresh instance of BaseModel for each test method.
        """
        self.check_inst = BaseModel()

    def test_init(self):
        """
        Test the initialization of BaseModel attributes.
        """
        self.assertIsNotNone(self.check_inst.id)
        self.assertIsInstance(self.check_inst.id, str)

        self.assertIsInstance(self.check_inst.created_at, datetime)
        self.assertIsInstance(self.check_inst.updated_at, datetime)

        createdAt = self.check_inst.created_at
        updatedAt = self.check_inst.updated_at
        self.assertEqual(updatedAt, createdAt)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        check_updated_at = self.check_inst.updated_at
        self.check_inst.save()
        self.assertNotEqual(check_updated_at, self.check_inst.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        dict_instance = self.check_inst.to_dict()
        self.assertIn('__class__', dict_instance)
        self.assertEqual(dict_instance['__class__'], 'BaseModel')
        self.assertIn('id', dict_instance)
        self.assertIn('created_at', dict_instance)
        self.assertIn('updated_at', dict_instance)
        self.assertEqual(dict_instance['id'], self.check_inst.id)

        createdAt = self.check_inst.created_at.isoformat()
        updatedAt = self.check_inst.updated_at.isoformat()
        self.assertEqual(dict_instance['created_at'], createdAt)
        self.assertEqual(dict_instance['updated_at'], updatedAt)
