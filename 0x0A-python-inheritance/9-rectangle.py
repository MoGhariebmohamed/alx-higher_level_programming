#!/usr/bin/python3
"""module for class"""


class BaseGeometry:
    """an empty class"""

    def area(self):
        """
        this function to raise message
        Args:
        return true if ok other False
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this function to raise more erorr
        Args:
            name: the attribute name
            value: the attribute value
        raise erorr
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """an empty class"""

    def __init__(self, width, height):
        """the initiating function for height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __init__(self, width, height):
        """the initiating function for height and width"""
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
        self.__width = width
        self.__height = height

    def area(self):
        """print area"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self__height))
