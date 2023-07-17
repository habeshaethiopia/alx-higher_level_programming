#!/usr/bin/python3
"""The module contain the class"""
from base import Base


class Rectangle(Base):
    """The class doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constractor"""
        self.__width = width
        self.__height = height
        super().__init__(id)
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter  height"""
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter x"""
        self.__y = y
