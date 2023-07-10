#!/usr/bin/python3
"""the modile document"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class squre"""

    def __init__(self, size):
        """constractor"""
        self.integer_validator("size", size)
        self.size = size

    def area(self):
        """the area"""
        return self.size**2
