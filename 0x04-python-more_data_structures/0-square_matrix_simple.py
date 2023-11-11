#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        sqr_m = lambda y: y ** 2
        new_mat.append(list(map(sqr_m, i)))
    return new_mat
