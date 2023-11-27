#!/usr/bin/python3
"""its for defines a rectungler"""


class Rectangle:
    """for rectungler dimensions"""
    def __init__(self, width=0, height=0):
        """for initiate the dims

        Arg:
            width: the rectungler width
            height: the rectungler height"""
        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        """the getter for value"""
        return (self.__width__)

    @width.setter
    def width(self, value):
        """the setter for width values"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """for getting the height"""
        return (self.height)

    @height.setter
    def height(self, value):
        """for setting values"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif (width < 0):
            raise ValueError("height must be >= 0")
        self.height = value
