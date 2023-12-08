#!/usr/bin/python3
"""
FileStorage module.
"""

import json
from datetime import datetime
from os.path import isfile
import sys
import os
import models
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
            if not isinstance(obj, dict):
                serialized_objects[key] = obj.to_dict()
            else:
                serialized_objects[key] = obj
                serialized_objects[key]['created_at'] = str(obj['created_at'])
                serialized_objects[key]['updated_at'] = str(obj['updated_at'])

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name = value['__class__']
                del value['__class__']
                obj_instance = eval(class_name)(**value)
                self.new(obj_instance)
        except FileNotFoundError:
            return


# storage = FileStorage()
# storage.reload()
