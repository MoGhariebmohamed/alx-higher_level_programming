#!/usr/bin/python3
"""this module Write a function that returns the JSON of string object"""

import json


def from_json_string(my_str):
    """
    the function to JSON of object
    Args:
        my_obj: the object of class
    """
    return (json.loads(my_str))
