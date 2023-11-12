#!/usr/bin/python3
"""Module to manage state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class to manage state"""

    name: str = ""
