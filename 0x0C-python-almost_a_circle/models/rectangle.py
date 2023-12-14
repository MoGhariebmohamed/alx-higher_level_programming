#!/usr/bin/python3
"""for inhent class from base"""

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
        super.__init__(id)
