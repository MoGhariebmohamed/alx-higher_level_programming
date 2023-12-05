#!/usr/bin/python3
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
    else:
        return False
