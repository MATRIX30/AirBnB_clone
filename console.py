#!/usr/bin/python3
"""command interpreter(console) for AirBnB"""

import cmd
from typing import IO
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage

classes = ["BaseModel", "User","Place",
        "State", "City", "Amenity" , "Review"]

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
        
        all_objects = storage.all()
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
        
        all_objects = storage.all()
        for key in all_objects.keys():
            class_name, id = key.split(".")
            if args[0] == class_name and args[1] == id:
                del all_objects[key]
                storage.save()
                return
        print("** no instance found **")
       
    def do_all(self, line):
        """
        Prints all string representation of all 
        instances based or not on the class name.
        """
        args = []
        args = line.split()
        all_objects = storage.all()
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
                        
    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"
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
        key = '.'.join([args[0], args[1]])
        all_objects = storage.all()
        if key not in all_objects.keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        selected_instance = all_objects[key]
        print(type(selected_instance))
        print(selected_instance)
        if args[2] not in selected_instance.to_dict().keys():
            print("** value missing **")
            return
        if len(args) > 4:
            args = args[:4]
        setattr(selected_instance,args[2],args[3])
        storage.save()
        
        
              

if __name__ == "__main__":
    HBNBCommand().cmdloop()