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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """to set privete attributes"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """to set privete x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints # in stdout the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for xx in range(self.y):
            print("")
        for hh in range(self.__height):
            for yy in range(self.x):
                print(" ", end="")
            for ww in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args):
        """
        assigns an argument to each attribute

        Args:
            args: the input unlimited
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attr[i], arg)

    def __str__(self):
        """method so that it returns id"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))
