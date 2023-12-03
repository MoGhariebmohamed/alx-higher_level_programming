#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    the matrix div function return two matrix_divided

    Args:
        matrix: the matrix
        div: the divission value
    Return:
        list: divided matrix
    """
    size = None
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for le in matrix:
        if type(le) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(le)
        elif size != len(le):
            raise TypeError("Each row of the matrix must have the same size")
        for i in le:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix(
                    list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in le] for le in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
