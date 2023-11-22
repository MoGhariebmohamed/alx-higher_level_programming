#!/usr/bin/python3
"""its for defines a square"""


class Square:
    """for squre dimensions"""

    def __init__(self, size=0):
        """lets initiate new square

        Args:
            size : For getting  size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """to retrive the size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """it's the setter of value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """for the area of the square"""
        return (self.__size * self.__size)
