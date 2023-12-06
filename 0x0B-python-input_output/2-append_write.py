#!/usr/bin/python3
"""this module Write a function that appends a string at end of a text file"""


def append_write(filename="", text=""):
    """
    the function to open
    Args:
        filename: the object of class
    """
    with open(filename, "a", encoding="utf-8") as x:
        return (x.write(text))
