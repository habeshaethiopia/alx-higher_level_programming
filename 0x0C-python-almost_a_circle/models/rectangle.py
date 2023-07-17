#!/usr/bin/python3
"""The module contain the class"""
from base import Base


class Rectangle(Base):
    """The class doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constractor"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        super().__init__(id)
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter  height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter x"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """the area doc"""
        return self.__width * self.__height

    def display(self):
        """doc for the doc"""
        for Y in range(self.__y):
            print()
        for i in range(self.__height):
            for X in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """the string Notation"""
        return "[Rectangle] ("+str(self.id) + ") "+str(self.__x)+"/"+str(self.__y)+" - "+str(self.__width)+"/"+str(self.__height)

    def update(self, *args):
        """afunction update"""
        if args is not None:
            if args[0]:
                self.id = args[0]
            if len(args) > 1:
                if args[1]:
                    self.__width = args[1]
            if len(args) > 2:
                if args[2]:
                    self.__height = args[2]
            if len(args) > 3:
                if args[3]:
                    self.__x = args[3]
            if len(args) > 4:
                if args[4]:
                    self.__y = args[4]
