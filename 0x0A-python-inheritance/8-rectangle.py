#!/usr/bin/python3
"""the modile document"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """aclass inherit from base Geometry"""

    def __init__(self, width, height):
        """The constractor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
