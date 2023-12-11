#!/usr/bin/python3
"""
Module of Unittests
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """
    def test_path_atribute(self):
        """
        test path
        """
        pass

    def test_class_obj(self):
        """
        Test class obj
        """
        pass

    def setUp(self):
        """
        Set up a clean environment for each test.
        """
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test.
        """
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all(self):
        """
        Test the 'all' method
        """
        pass

    def test_new(self):
        """
        Test the 'new' method
        """
        self.file_storage.new(self.base_model)
        objects = self.file_storage.all()
        self.assertIn('BaseModel.' + self.base_model.id, objects)

    def test_save_and_reload(self):
        """
        Test the 'save' and 'reload' methods
        """
        pass


if __name__ == '__main__':
    unittest.main()
