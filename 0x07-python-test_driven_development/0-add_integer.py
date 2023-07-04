#!/usr/bin/python3
def add_integer(a, b=98):
    
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a= int(a)
    if type(b) != int:
        raise TypeError("a must be an integer")
    elif type(b) == float:
        b= int(b)
    return a+b
