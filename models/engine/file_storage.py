#!/usr/bin/python3

"""
Define class Modules for the storing file
"""
import json
import os.path
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """
    class that handles serialization and
    deserialization of instances to/from JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all stored objects.

        Returns:
            dict: A dictionary of objects with keys as "<class name>.id".
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to be added to the storage.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes objects to the JSON file.
        """
        dict_data = {}
        for key, value in self.__objects.items():
            dict_data[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dict_data, file)

    def reload(self):
        """
        Deserializes objects from the JSON file if it exists.
        Does nothing if the file doesn't exist; no exceptions are raised.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                my_obj_dict = json.load(file)
                my_obj_dict = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in my_obj_dict.items()
                }

                FileStorage.__objects = my_obj_dict

    def classes(self):
        """
        Returns a dictionary of available classes.
        """
        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return classes_dict
