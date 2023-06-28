#!/usr/bin/python3
"""This modeule contain a square class"""


class square:
    """A square class """

    def __init__(self, size=0):
        """Initialization of the class"""
        try:
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError as t:
            print(t)
        except ValueError as v:
            print(v)
