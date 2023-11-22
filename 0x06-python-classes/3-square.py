#!/usr/bin/python3
"""its for defines a square"""


class Square:
    """for squre dimensions"""

    def __init__(self, size=0):
        """lets initiate new square

        Args:
            size : For getting  size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            """for the area of the square"""
            return (self.__size * self.__size)
