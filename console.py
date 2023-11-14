#!/usr/bin/python3
"""command interpreter(console) for AirBnB"""

import cmd
import re
from shlex import split
from typing import IO
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


def line_split(arg):
    curl_brace = re.search(r"\{(.*?)\}", arg)
    square_brace = re.search(r"\[(.*?)\]", arg)
    if curl_brace is None:
        if square_brace is None:
            # print([i.strip(",") for i in split(arg)])
            return [item.strip(",") for item in split(arg)]
        else:
            pattern = split(arg[: square_brace.span()[0]])
            res = [item.strip(",") for item in pattern]
            res.append(square_brace.group())
            return res
    else:
        pattern = split(arg[: curl_brace.span()[0]])
        res = [i.strip(",") for i in pattern]
        res.append(curl_brace.group())
        return res


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
        args = line.split()
        all_objects = storage.all()
        objs = []
        if not args:
            # print([str(value) for value in all_objects.values()])
            for key in all_objects.keys():
                objs.append(str(all_objects[key]))
                # print([str(all_objects[key])])
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
                        # print(all_objects[key])
                        objs.append(str(all_objects[key]))
        print(objs)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = []
        # ar = []
        # ar = line.split()
        args = line_split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = ".".join([args[0], args[1]])
        all_objects = storage.all()
        if key not in all_objects.keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        selected_instance = all_objects[key]

        # if args[2] not in selected_instance.to_dict().keys():
        # if they are just 3 arguments
        if len(args) == 3:
            print("** value missing **")
            return

        if len(args) == 4:
            if args[2] in selected_instance.__class__.__dict__.keys():
                argtype = type(selected_instance.__class__.__dict__[args[2]])
                selected_instance.__dict__[args[2]] = argtype(args[3])
            else:
                selected_instance.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            for k, v in eval(args[2]):
                if (k in selected_instance.__class__.__dict__.keys()) and type(
                    selected_instance.__class__.__dict__[k]
                ) in [str, int, float]:
                    argtype = type(selected_instance.__class__.__dict__[k])
                    selected_instance.__dict__[k] = argtype(v)
                else:
                    selected_instance.__dict__[k] = v
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
