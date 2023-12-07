#!/usr/bin/python3
"""this module Write a function that returns the JSON of string object"""


    def class_to_json(obj):
    """
    the function to JSON of object
    Args:
        my_obj: the object of class
    """
    return (obj.__dict__)
