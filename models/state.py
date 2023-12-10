#!/usr/bin/python3
"""
Module for State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class with attributes:
    - name: string (empty string)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of State.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
