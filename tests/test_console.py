#!/usr/bin/python3
"""Test Module for console.py """
import os
import console
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Test for HBNB command interpreter."""

    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """delete the temporal file.json after testing """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_prompt_str(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    # testing quit() method
    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    # testing EOF() method
    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    # testing show method both <className>.show(<id>) and show()
    def test_show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            # self.assertEqual(correct, output.getvalue().strip())

    # testing destroy method both <className>.destroy(<id>) and destroy()
    def test_destroy(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            # self.assertEqual(correct, output.getvalue().strip())

    # testing all method <className>.all()
    def test_all(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    # testing update method both <className>.update(<id>) and update()
    def test_update(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            """self.assertEqual(correct, output.getvalue().strip())"""

    # testing count method <className>.count()
    def test_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            """self.assertEqual("0", output.getvalue().strip())"""


if __name__ == "__main__":
    unittest.main()
