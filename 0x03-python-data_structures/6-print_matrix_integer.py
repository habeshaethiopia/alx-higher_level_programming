#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    d = " "
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end=d)
                if j == len(matrix[i])-2:
                    d = "\n"
                else:
                    d = " "
    else:
        print()
