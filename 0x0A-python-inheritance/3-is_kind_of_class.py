#!/usr/bin/python3
"""module to identify the instance of inherent class"""


def is_kind_of_class(obj, a_class):
    """ 
    this function to exactly an instance of class
    Args:
        obj: the object itself
        a_class: the class to be checked
    return true if ok other False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
