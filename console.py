#!/usr/bin/python3
"""command interpreter(console) for AirBnB"""


import cmd
from typing import IO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
classes = ["BaseModel", "User"]

class HBNBCommand(cmd.Cmd):
    """main console class"""
    prompt = "(hbnb) "
    
    
    
    def do_quit(self, command):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, command):
        """ EOF command to exit the program when
        an end of file(EOF) character is reached 
        """
        return True
    
    def emptyline(self):
        """called when the user enters nothing and hits enter"""
        return ""
    
    def postloop(self):
        """called  when the loop stops"""
        return
    
    def do_create(self, line):
        """Creates a new instance of a class"""
        args = []
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)
    
    
    def do_show(self, line):
        """
        prints the string representation of and instance
        base on the class name and id
        """
        args = []
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        all_objects = models.storage.all()
        for key in all_objects.keys():
            class_name, id = key.split(".")
            if args[0] == class_name and args[1] == id:
                print(all_objects[key])
                return
        print("** no instance found **")
    
    def do_destroy(self, line):
        """
         Deletes an instance based on the class name and 
         id (save the change into the JSON file)
        """
        args = []
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        all_objects = models.storage.all()
        for key in all_objects.keys():
            class_name, id = key.split(".")
            if args[0] == class_name and args[1] == id:
                del all_objects[key]
                models.storage.save()
                return
        print("** no instance found **")
       
    def do_all(self, line):
        """
        Prints all string representation of all 
        instances based or not on the class name.
        """
        args = []
        args = line.split()
        all_objects = models.storage.all()
        if not args:
            for key in all_objects.keys():
                print(all_objects[key])
        else:
            # elimintate any duplicate class name
            args = set(args)
            args = list(args)
            for arg in args: 
                if arg not in classes:
                    print("** class doesn't exist **")
                    return
                for key in all_objects.keys():
                    class_name, id = key.split(".")
                    if class_name == arg:
                        print(all_objects[key])
                        
                
            
            

if __name__ == "__main__":
    HBNBCommand().cmdloop()