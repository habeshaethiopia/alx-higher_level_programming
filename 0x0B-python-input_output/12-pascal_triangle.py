#!/usr/bin/python3
"""the module doc"""


def pascal_triangle(n):
    """the Technical interview preparation"""
    lis = []
    if n <= 0:
        return
    else:
        for i in range[n]:
            row = []
            for j in range[i]:
                if j == i[(len[i] - 1)] or j == 0:
                    row.append(1)
                else:
                    row.append(lis[i-1][j-1]+lis[i-1][j])
            lis.append(row)
        return lis
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print_triangle(pascal_triangle(5))
