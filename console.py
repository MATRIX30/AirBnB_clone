#!/usr/bin/python3
"""command interpreter(console) for AirBnB"""


import cmd
from typing import IO
class HBNBCommand(cmd.Cmd):
    """main console class"""
    prompt = "(hbnb) \n"
    
    def do_quit(self, command):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, command):
        """ EOF command to exit the program when
        an end of file(EOF) character is reached 
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()