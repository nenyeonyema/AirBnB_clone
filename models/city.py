#!/usr/bin/python3
"""
Module for City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class with attributes:
    - state_id: string (empty string): it will be the State.id
    - name: string (empty string)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of City.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
