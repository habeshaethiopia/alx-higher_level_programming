#!/usr/bin/python3
"""the module document"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class squre"""

    def __init__(self, size):
        """constractor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """the area"""
        return self.__size**2

    def __str__(self):
        """The string"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
