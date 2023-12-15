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
        super().__init__(size, size, x, y)

    def __str__(self):
        """method so that it returns id"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
