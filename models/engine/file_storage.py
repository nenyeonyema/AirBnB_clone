#!/usr/bin/python3
"""
FileStorage module.
"""

import json
from datetime import datetime
from os.path import isfile
import sys
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            class_name = obj.__class__.__name__
            obj_id = obj.id
            new_key = "{}.{}".format(class_name, obj_id)
            serialized_objects[new_key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    obj_dict = json.load(file)
                except ValueError:
                    obj_dict = {}

            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj


storage = FileStorage()
storage.reload()
