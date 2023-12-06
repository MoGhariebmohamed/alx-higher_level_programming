#!/usr/bin/python3
"""this module Write a function that writes an Object to a text file JSON"""

import json


def save_to_json_file(my_obj, filename):
    """
    the function to JSON of object
    Args:
        my_obj: the object of class
        filename: name of the file
    """
    with open(filename, "w") as x:
        return (json.dump(my_obj))
