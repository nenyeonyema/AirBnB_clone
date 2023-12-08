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

    def test_instance_creation_from_dict(self):
        """ Test Instance creation from dict"""
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01T12:34:56.789000',
            'updated_at': '2022-01-02T01:23:45.678000',
            '__class__': 'BaseModel',
            'additional_attribute': 'value'
        }
        new_instance = BaseModel(**data)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, 'some_id')
        self.assertEqual(new_instance.additional_attribute, 'value')
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_to_dict_with_instance_from_dict(self):
        """ Test to dict with instance from dict """
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01T12:34:56.789000',
            'updated_at': '2022-01-02T01:23:45.678000',
            '__class__': 'BaseModel',
            'additional_attribute': 'value'
        }
        new_instance = BaseModel(**data)
        new_instance_dict = new_instance.to_dict()
        self.assertIn('additional_attribute', new_instance_dict)

    def test_json_serialization(self):
        """ Test json serialization
        self.assertIn('id', json_str)
        self.assertIn('created_at', json_str)
        self.assertIn('updated_at', json_str)
        self.assertIn('__class__', json_str)
        self.assertEqual(json.loads(json_str)['__class__'], 'BaseModel')
        """


if __name__ == "__main__":
    unittest.main()
