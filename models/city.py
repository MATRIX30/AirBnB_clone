#!/usr/bin/python3
"""module to manage cities"""
from models.base_model import BaseModel
class City(BaseModel):
    """class to manage City"""
    state_id:str = ""
    name:str = ""
