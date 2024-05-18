#!/usr/bin/python3
"""defines all common attributes/methods """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """a class BaseModel that defines all common -
    attributes/methods for other classes
    id: string - assign with an uuid when an instance is created:
    created_at: datetime -
    assign with the current datetime when an instance is created
    updated_at: datetime -
    assign with the current datetime when an instance is created
    and it will be updated every time you change your object"""
    def __init__(self, *args, **kwargs):
        """Initializes public instance attributes and methods
        *args won’t be used
        **kwargs: key value pair for attributes or object created"""
        dtformat = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, dtformat)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns the string representation of the object"""
        classname = self.__class__.__name__
        return f"[{classname}] ({self.id}) {self.__dict__}"

    def save(self):
        """"updates the public instance attribute updated_at -
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values -
        of __dict__ of the instance:"""
        dictionary = self.__dict__.copy()
        date_attr = ['created_at', 'updated_at']
        for key, value in dictionary.items():
            if key in date_attr:
                dictionary[key] = value.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
