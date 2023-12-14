#!/usr/bin/python3
"""for inhent class from base"""
from models.base import Base

class Rectangle(Base):
    """inhent class from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            for setter and getter of attributes

            Args:
                width: rectangle width
                height: rectangle height
                x: axis x location
                y: axis  location
                id: id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """to set width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """to set privete attributes"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """to set privete x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """to set privete y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
