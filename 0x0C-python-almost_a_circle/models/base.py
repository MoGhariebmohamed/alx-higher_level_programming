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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        that writes the JSON string representation of list_objs

        Args:
            list_objs: a list of instances who inherits of Base
            cls: class method
        """
        FileName = cls.__name__ + ".json"
        with open(FileName, "w", encoding="utf-8") as OpenFile:
            if list_objs is None:
                OpenFile.write("[]")
            else:
                MakeDict = [op.to_dictionary() for op in list_objs]
                OpenFile.write(Base.to_json_string(MakeDict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation

        Args:
            json_string: the string from json
        """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        Args:
            dictionary: can be thought of as a double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                NewDict = cls(1, 1)
            else:
                NewDict = cls(1)
            NewDict.update(**dictionary)
            return NewDict

    @classmethod
    def load_from_file(cls):
        """returns a list of instances file of JSON strings"""
        FileName = str(cls.__name__) + ".json"
        try:
            with open(FileName, "r", encoding="utf-8") as OpenFile:
                ListDicts = Base.from_json_string(OpenFile.read())
                return [cls.create(**dd) for dd in ListDicts]
        except IOError:
            return []
