#!/usr/bin/python3
"""
Test cases for the FileStorage class.
"""

import os
import json
import models
import unittest

from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test resources.
        """
        self.file_path = 'file.json'
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up test resources.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_instance(self):
        """
        Test creating a new instance of FileStorage.
        """
        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        """
        Test the 'all' method returns a dictionary.
        """
        all_data = self.storage.all()
        self.assertIsInstance(all_data, dict)


if __name__ == "__main__":
    unittest.main()
