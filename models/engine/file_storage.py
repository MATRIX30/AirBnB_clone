#!/usr/bin/python3
""" File storage module """


import json
from json.decoder import JSONDecodeError
import os
from models.base_model import BaseModel

class FileStorage:
    """ 
    file storage class FileStorage that serializes
    instances to a JSON file and deserializes JSON
    file to instances:
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """ returns the dictionary objects"""
        return FileStorage.__objects
    def new(self, obj):
        """
         sets in __objects the obj with
         key <obj class name>.id
         
         Args:
            obj(object_type): the object to be set
        """
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        # if key in self.__objects.keys():
        #FileStorage.__objects[key] = obj.to_dict()
        FileStorage.__objects[key] = obj
        
    def save(self):
        """
        serializes __objects to the JSON
        file (path: __file_path)
        """

        if bool(FileStorage.__objects) and len(FileStorage.__file_path) > 0:
            # convert each obj of __objects to its dict representation 
            data = {
                key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            #data = json.dumps(FileStorage.__objects)
            # converting the data dict to json string and writing it to __file_path
            with open(FileStorage.__file_path, 'w') as file_handler:
                json.dump(data, file_handler)
                
       
    def reload(self):
        """
         deserializes the JSON file to __objects 
         (only if the JSON file (__file_path) exists ;
         otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as file_handler:
                    # self.__objects = json.load(file_handler)
                    loaded_obj = json.load(file_handler)
            except (JSONDecodeError):
                """do nothing if decode error occurs"""
                return
            res_dict = {}
            #self.__objects = loaded_obj
            for obj_id in loaded_obj.keys():
                obj = loaded_obj[obj_id]
                loaded_instance=eval(obj["__class__"])(**obj)
                res_dict[obj_id] = loaded_instance
            FileStorage.__objects = res_dict