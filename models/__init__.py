#!/usr/bin/python3
"""
__init__ file to make dicectory a package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
