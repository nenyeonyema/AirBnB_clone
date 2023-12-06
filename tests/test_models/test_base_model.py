#!/usr/bin/python3
"""
Unittests for BaseModel class.
"""

import os
import json
import models
import unittest
import sys
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
sys.path.insert(0, './models')


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def test_create_instance(self):
        """
        Test creating an instance of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of BaseModel.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_representation(self):
        """
        Test the string representation of BaseModel.
        """
        my_model = BaseModel()
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}"
                         .format(my_model.id, my_model.__dict__))

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        expected_keys = ['id', 'created_at',
                         'updated_at', 'name', 'my_number', '__class__']
        self.assertEqual(sorted(my_model_dict.keys()), sorted(expected_keys))
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
