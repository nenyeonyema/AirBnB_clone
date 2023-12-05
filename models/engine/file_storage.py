#!/usr/bin/python3
"""
FileStorage module.
"""

import json

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
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
