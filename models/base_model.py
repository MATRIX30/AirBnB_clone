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

    def __init__(self) -> None:
        """Base Model constructor"""
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

    def to_dic(self):
        """
        returns dictionary containing all keys/values
        of __dict__ of the instance
        """
        pass
