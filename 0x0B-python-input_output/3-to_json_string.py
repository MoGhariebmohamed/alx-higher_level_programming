#!/usr/bin/python3
"""this module Write a function that returns the JSON of string object"""

import json


def to_json_string(my_obj):
    """
    the function to JSON of object
    Args:
        my_obj: the object of class
    """
    return (json.dumps(my_obj))
