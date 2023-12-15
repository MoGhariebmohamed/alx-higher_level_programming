#!/usr/bin/python3
""" for base class"""
import json


class Base:
    """a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        goal of it is to manage id attribute

        Args:
            id: public instance attribute id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        the static method eturns the JSON string of list_dictionaries

        Args:
            list_dictionaries: the list dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
