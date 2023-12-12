#!/usr/bin/python3
class Base:
"""a base class"""


    __nb_objects = 0
    def __init__(self, id=None):
        """
         goal of it is to manage id attribute
         
         Args:
            id: public instance attribute id
        """
        if id != None:
            self.id = id
        else:
           self.id = Base.__nb_objects + 1


