#!/usr/bin/python3
"""its for defines a rectungler"""


class Rectangle:
    """for rectungler dimensions"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """for initiate the dims

        Arg:
            width: the rectungler width
            height: the rectungler height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """method to user friendly represent"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        if (self.width != 0 and self.height != 0):
            prtt = ((str(self.print_symbol) * self.width + "\n")
                    * self.height)[:-1]
            return (prtt)

    def __repr__(self):
        """for developer check object and methods"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """method to delte"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (rect_2.area() > rect_1.area()):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """method return equal pram"""
        return (cls(size, size))
