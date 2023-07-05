#!/usr/bin/python3
#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
