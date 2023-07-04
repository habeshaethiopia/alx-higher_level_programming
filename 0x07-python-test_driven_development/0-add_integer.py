#!/usr/bin/python3
"""A module with afnction to add two integers"""


def add_integer(a, b=98):
    """ this function is to add 
    two integers and handling all the
    posible test cases
    """
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a = int(a)
    if type(b) != int:
        raise TypeError("a must be an integer")
    elif type(b) == float:
        b = int(b)
    return a+b
