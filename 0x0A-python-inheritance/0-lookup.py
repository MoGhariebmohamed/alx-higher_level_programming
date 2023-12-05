#!/usr/bin/python3
"""this module to return all methods and attributes"""


def lookup(obj):
    """
    the function to return all methods
    Args:
        obj: the object of class
        """
    return dir(obj)
