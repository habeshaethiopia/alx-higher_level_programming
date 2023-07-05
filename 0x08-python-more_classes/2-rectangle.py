#!/usr/bin/python3
"""This is a module for a class Rectangle"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__height*self.__width

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width+self.__height)
