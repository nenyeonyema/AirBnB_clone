#!/usr/bin/python3
"""
Importing FileStorage, setting it equal to storage, calling reload
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
