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
