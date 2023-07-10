#!/usr/bin/python3
"""the modile document"""


class Rectangle(BaseGeometry):
    """aclass inherit from base Geometry"""

    def __init__(self, width, height):
        """The constractor"""
        self._width = width
        self._height = height
        super.integer_validator("width", width)
        super.integer_validator("height", height)
