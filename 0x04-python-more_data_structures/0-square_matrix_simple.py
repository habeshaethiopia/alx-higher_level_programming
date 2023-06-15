#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    li = []
    for i in matrix:
        li.append(list(map(lambda x: x**2, i)))
    return li
