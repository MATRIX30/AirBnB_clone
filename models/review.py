#!/bin/usr/python3
"""Module to manage reviews"""
from models.base_model import BaseModel
class Review(BaseModel):
    """class to manage review"""
    place_id:str = ""
    user_id:str = ""
    text:str = ""
