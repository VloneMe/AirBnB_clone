#!/usr/bin/python3

"""
A Module for FileStorage and baseModel linking
"""
from models.engine.file_storage import FileStorage

"""
Create the variable 'storage', an instance of FileStorage
"""
storage = FileStorage()

"""
Call the 'reload()' method on this variable
"""
storage.reload()
