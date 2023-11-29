#!/usr/bin/python3
"""its for defines a rectungler"""


class Rectangle:
    """for rectungler dimensions"""
    def __init__(self, width=0, height=0):
        """for initiate the dims

        Arg:
            width: the rectungler width
            height: the rectungler height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter for value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """the setter for width values"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """for getting the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """for setting values"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """to get the area of rectungler"""
        return (self.width * self.height)

    def perimeter(self):
        """to get permiter of the rectungler"""
        Perm = 2 * (self.width + self.height)
        if (self.width == 0 or self.height == 0):
            return (0)
        else:
            return (Perm)
