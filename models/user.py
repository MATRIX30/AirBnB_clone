#!/usr/bin/python3
"""Module to manage users"""

from models.base_model import BaseModel
class User(BaseModel):
    """class to manage Users"""
    email:str = ""
    password:str = ""
    first_name:str = ""
    last_name:str = ""
    
    