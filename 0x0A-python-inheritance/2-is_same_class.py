#!/usr/bin/python3
"""this module to identify instance of parent class"""


def is_same_class(obj, a_class):
    """
    this function to exactly an instance of class
    Args:
        obj: the object itself
        a_class: the class to be checked
    return true if ok other False
    """
    if (type(obj) == a_class):
        return True
    return False
