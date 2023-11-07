#!/usr/bin/python3
"""
base model to be inherited and used by other classes and modules
"""
import uuid
import datetime


class BaseModel:
    """
    class for Base model defining all shared attributes
    and methods used by other classes in the AirBnB project
    """

    def __init__(self, *args, **kwargs) -> None:
        """Base Model constructor"""
        if bool(kwargs):
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.datetime.strptime(kwargs['created_at'],"%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],"%Y-%m-%dT%H:%M:%S.%f")   
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at


    def __str__(self) -> str:
        """prints out the str representation of base model object"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        updates the public instance attribute
        updated_at with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns dictionary containing all keys/values
        of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat(
            sep="T", timespec="auto"
        )
        self.__dict__["updated_at"] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"
        )
        return self.__dict__
