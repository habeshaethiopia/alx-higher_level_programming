#!/usr/bin/python3
"""This modeule contain a square class"""


class Square:
    """A square class """

    def __init__(self, size=0):
        """Initialization of the class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ a function which returns the Area"""
        return self.__size*self.__size

    def size(self):
        """ Function that returns the size of the square"""
        return self.__size
