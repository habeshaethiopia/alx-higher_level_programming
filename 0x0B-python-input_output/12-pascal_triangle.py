#!/usr/bin/python3
"""the module doc"""


def pascal_triangle(n):
    """the Technical interview preparation"""
    lis = []
    if n <= 0:
        return
    else:
        for i in range(1, n+1):
            row = []
            for j in range(i):
                if j == i-1 or j == 0:
                    row.append(1)
                else:
                    row.append(lis[i-2][j-1]+lis[i-2][j])
            lis.append(row)
        return lis
