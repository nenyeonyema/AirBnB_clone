#!/usr/bin/python3
"""
Module for Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class with attributes:
    - place_id: string (empty string): it will be the Place.id
    - user_id: string (empty string): it will be the User.id
    - text: string (empty string)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of Review.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""