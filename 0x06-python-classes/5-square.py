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

    @property
    def size(self):
        """ Function that returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ function to print asquare compoas of "#" symbol"""
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
