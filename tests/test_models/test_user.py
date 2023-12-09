#!/usr/bin/python3
"""
Test module for the User class.
"""

import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up for the test."""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john.doe@example.com"
        self.user.password = "password123"

    def tearDown(self):
        """Clean up after the test."""
        del self.user

    def test_instance(self):
        """Test if user is an instance of User."""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test if user has the required attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attribute_types(self):
        """Test if user attributes have the correct types."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save_method(self):
        """Test if save method saves the instance to the storage."""
        models.storage.reload()
        initial_count = len(models.storage.all())
        new_user = User()
        new_user.email = "newuser@example.com"
        new_user.password = "newpassword"
        new_user.first_name = "New"
        new_user.last_name = "User"
        new_user.save()

    def test_to_dict_method(self):
        """
        Test if to_dict method returns a
        dictionary with proper attributes.
        """
        user_dict = self.user.to_dict()
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_str_method(self):
        """Test if the __str__ method returns a string representation."""
        string = str(self.user)
        self.assertIsInstance(string, str)


if __name__ == '__main__':
    unittest.main()
