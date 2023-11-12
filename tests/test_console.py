#!/usr/bin/python3
"""
Test module for console intepreter
"""

import imp
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test class for console"""

    def test_help_quit(self):
        """Tests the help command."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = "Quit command to exit the program\n"
        self.assertEqual(s, f.getvalue())


if __name__ == "__main__":
    unittest.main()
