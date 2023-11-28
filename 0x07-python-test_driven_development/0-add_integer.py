#!/usr/bin/python3
"""its for add two integers"""

def add_integer(a, b=98):
    """
    the add function return sub of a and b
    """
    if (type(a) == float):
        a = int(a)
    if type(b) == float:
        b = int(b)

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b)  not in (int, float):
        raise TypeError("b must be an integer")
        

    return (a + b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
