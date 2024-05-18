#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """A class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances:"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists: otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with (FileStorage.__file_path) as file:
                dict_obj = json.load(file)
                for value in dict_obj.values():
                    cls = value['__class__']
                    self.new(eval(cls)(**value))
        except Exception:
            pass
