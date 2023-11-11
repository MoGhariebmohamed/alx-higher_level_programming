#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        def sqr_m(y):
            y = y ** 2
            return y
        new_mat.append(list(map(sqr_m, i)))
    return new_mat
