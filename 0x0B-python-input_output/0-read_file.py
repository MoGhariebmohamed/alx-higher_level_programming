#!/usr/bin/python3
"""this module Write a function that reads a text file"""


def read_file(filename=""):
    """
    the function to open
    Args:
        filename: the object of class
        """
    with open(filename, "r", encoding="utf-8") as x:
        print(x.read(), end="")
