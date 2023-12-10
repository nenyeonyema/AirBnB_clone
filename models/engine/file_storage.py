#!/usr/bin/python3
"""
FileStorage module.
"""

from datetime import datetime
import json
from os.path import isfile
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    FileStorage class.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        self.__objects.update({obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file."""
        ser_obj = {}
        for key in FileStorage.__objects.keys():
            if type(FileStorage.__objects[key]) is not dict:
                ddict = FileStorage.__objects[key].to_json()
                ser_obj({key: ddict})
            else:
                ser_obj.update({key: ddict[key]})
                ser_obj.update({'created_at': str(ser_obj[key]
                                ['created_at'])})
                ser_obj.update({'updated_at': str(ser_obj[key]
                                ['updated_at'])})
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(ser_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to __object.
        """
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                load = json.load(f)
                for key in load.keys():
                    check_name = load[key]['__class__']
                    new_base = self.__checker(check_name,
                                              (load[key]))
                    load.update({key: new_base})

        d_dict = {"Amenity": Amenity, "BaseModel": BaseModel,
                  "City": City, "Place": Place, "Review": Review,
                  "State": State, "User": User}
        if Class not in d_dict.keys():
            print("** class doesn't exist **")
            return None
        else:
            return d_dict[Class]
