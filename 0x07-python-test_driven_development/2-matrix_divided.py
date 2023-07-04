#!/usr/bin/python3
""" module cantaining matrix_divided(matrix, div) function"""


def matrix_divided(matrix, div):
    """afunction which divide each element of a matrix"""
    Emess = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError(Emess)
    for r in matrix:
        if len(r) == 0:
            raise TypeError(Emess)
        for i in r:
            if type(i) != int and type(i) != float:
                raise TypeError(Emess)

    l = len(matrix[0])
    for r in matrix:
        if l == len(r):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_m = []
    for r in matrix:
        row = []
        for v in r:
            result = round(v/div, 2)
            row.append(result)
        new_m.append(row)
    return new_m
