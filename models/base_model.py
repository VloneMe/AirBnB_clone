#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class that provides common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Variable length argument list
            (not used in this implementation).
            **kwargs: Arbitrary keyword arguments.
                - If 'created_at' or 'updated_at' is provided,
                  convert their string representations to datetime objects.
                - If 'id' is not provided, generate a new UUID.
                - If 'created_at' and 'updated_at' are not provided,
                  set 'created_at' to current time.
        """
        if args or len(kwargs) == 0:
            """
            Create a new instance if not created from a dictionary
            representation
            """
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            """
            Add a call to 'new' method on storage for new instances
            """
            models.storage.new(self)
        else:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    timeFormat = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, timeFormat))
                else:
                    setattr(self, key, value)

            if 'id' not in kwargs:
                self.id = str(uuid4())

            if 'created_at' not in kwargs:
                self.created_at = datetime.now()

            if 'updated_at' not in kwargs:
                self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: Formatted string representation.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime.
        with Call save method of storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing keys/values of instance attributes.
        """
        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()
        return dict_instance

