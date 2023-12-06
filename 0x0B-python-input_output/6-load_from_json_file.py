#!/usr/bin/python3
"""this module Write a function creates an Object from a “JSON file"""

import json


def load_from_json_file(filename):
    """
    the function to JSON of object
    Args:
        filename: name of the file
    """
    with open(filename, "r") as x:
        return (json.loads(x.read()))
