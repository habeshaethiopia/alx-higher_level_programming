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
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.__width+self.__height)

    def __str__(self):
        """Get the string representation"""
        s = ""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return s
        for i in range(height):
            for j in range(width):
                s = s + "#"
            s = s + "\n"
        return s[:-1]

    def __repr__(self):
        """get string representation"""
        s = "Rectangle({}, {})".format(str(self.__width), str(self.height))
        return s
