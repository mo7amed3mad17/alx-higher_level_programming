#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s_list = []
    for row in matrix:
        s_list.append([x**2 for x in row])
    return s_list
