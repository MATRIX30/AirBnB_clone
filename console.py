#!/usr/bin/python3
"""command interpreter(console) for AirBnB"""

import cmd
import re
from typing import IO
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """main console class"""

    prompt = "(hbnb) "

    def do_quit(self, command):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, command):
        """EOF command to exit the program when
        an end of file(EOF) character is reached
        """
        print("")
        return True

    def emptyline(self):
        """called when the user enters nothing and hits enter"""
        return ""

    def postloop(self):
        """called  when the loop stops"""
        return

    def do_create(self, line: str):
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

    def do_show(self, line: str):
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

    def do_destroy(self, line: str):
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

    def do_all(self, line: str):
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

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


    def do_count(self, line: str):
        """
        counts the number of instances of a class
        Usage: count <className> or <className>.count()
        """
        args = []
        args = line.split()
        count = 0
        all_objs = storage.all()
        if bool(args) and len(args) == 1:
            for obj_id in all_objs.keys():
                if args[0] == obj_id.split(".")[0]:
                    count += 1
            print(count)
            return
        print("Usage: count <className>")

    def default(self, line: str):
        """
        Default method that executes when a command entered
        cant find a corresponding function to call or execute
        """
        commands = {
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "count": self.do_count,
        }
        dot = re.search(r"\.", line)
        if dot is not None:
            instruction = [line[: dot.span()[0]], line[dot.span()[1]:]]
            bracket = re.search(r"\((.*?)\)", instruction[1])
            if bracket is not None:
                cmd = [instruction[1][: bracket.span()[0]],
                       bracket.group()[1:-1]]

                if cmd[0] in commands.keys():
                    return commands[cmd[0]](f"{instruction[0]} {cmd[1]}")
        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
