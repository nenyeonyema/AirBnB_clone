#!/usr/bin/python3
"""
Module of Unittests
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up a clean environment for each test.
        """
        # Ensure that the test file does not exist initially
        self.remove_test_file()
        # Create a new FileStorage instance
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test.
        """
        # Remove the test file after each test
        self.remove_test_file()

    def remove_test_file(self):
        """
        Remove the test file if it exists.
        """
        test_file_path = FileStorage._FileStorage__file_path
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

    def test_all(self):
        """
        Test the all method of the FileStorage.
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        """
        Test the new method of the FileStorage.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn(f"BaseModel.{my_model.id}", all_objects)

    def test_reload_nonexistent_file(self):
        """
        Test that reloading a nonexistent file does not raise an exception.
        """
        # Remove the test file before reloading
        self.remove_test_file()

        # Create a new FileStorage instance for reloading
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()


if __name__ == '__main__':
    unittest.main()
