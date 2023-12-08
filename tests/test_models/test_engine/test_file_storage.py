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

    def test_new_model_save(self):
        """
        Test creating a new model, saving it,
        and checking if it exists in storage.
        """
        model = BaseModel()
        model.save()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        all_data = self.storage.all()

    def test_save_to_file(self):
        """
        Test saving a model to a file and checking if the file exists.
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_from_file(self):
        """
        Test saving a model, reloading storage,
        and checking if the model is still present.
        """
        model = BaseModel()
        model.save()
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        all_data = self.storage.all()


if __name__ == "__main__":
    unittest.main()
