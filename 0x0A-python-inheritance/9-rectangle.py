#!/usr/bin/python3
"""the modile document"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """aclass inherit from base Geometry"""

    def __init__(self, width, height):
        """The constractor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """impliment the area"""
        return self.__height * self.__width

    def __str__(self):
        """the string"""
        print("[Rectangle] {}/{}".format(str(self._width), str(self._height)))
