#!/usr/bin/python3
"""this module Write a function that reads a text file"""


def write_file(filename="", text=""):
    """
    the function to open
    Args:
        filename: the object of class
        text: the writen text
        """
    if (type(text) != str):
        text = str(text)
    with open(filename, "w", encoding="utf-8") as x:
            return (x.write(text))
