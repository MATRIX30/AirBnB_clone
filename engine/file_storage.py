#!/usr/bin/python3
""" File storage module """


import json
import os
class FileStorage:
    """ 
    file storage class FileStorage that serializes
    instances to a JSON file and deserializes JSON
    file to instances:
    """
    __file_path = ""
    __objects = {}
    
    def all(self):
        """ returns the dictionary objects"""
        return self.__objects
    def new(self, obj):
        """
         sets in __objects the obj with
         key <obj class name>.id
         
         Args:
            obj(object_type): the object to be set
        """
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        # if key in self.__objects.keys():
        self.__objects[key] = obj
        
    def save(self):
        """
        serializes __objects to the JSON
        file (path: __file_path)
        """
        if not bool(self.__objects):
            with open(self.__file_path, 'w') as file_handler:
                json.dump(self.__objects, file_handler)
       
    def reload(self):
        """
         deserializes the JSON file to __objects 
         (only if the JSON file (__file_path) exists ;
         otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file_handler:
                self.__objects = json.load(file_handler)
        