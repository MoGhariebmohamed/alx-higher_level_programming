#!/usr/bin/python3
"""a Square is a special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square is a special Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor square

        Args:
            size: the square size
            x: x-axis length
            y: y-axis empty length
            id: the Rectangle length
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the setter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """to set value for size"""
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute

        Args:
            args: the input unlimited
            kwargs: the dictinary of id and value
        """
        attr = ['id', 'size', 'x', 'y']
        if args != 0 and len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        elif kwargs != 0 and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """method so that it returns id"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
