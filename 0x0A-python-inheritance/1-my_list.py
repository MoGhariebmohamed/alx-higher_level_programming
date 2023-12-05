#!/usr/bin/python3
"""this for inherting class"""


class MyList(list):
    """
    inhernt class from list
    """
    def print_sorted(self):
        """
        method to print sorted list
        """
        print(sorted(self))
