#!/usr/bin/python3
"""the modile document"""


class BaseGeometry:
    """a New class"""

    def area(self):
        """the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Intiger Validater"""
        if type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
