#!/usr/bin/python3
"""the module"""
import math


class MagicClass():
    """The Magic class."""

    def __init__(self, radius=0):
        """Initalize the class."""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area getter"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calcu 2pi r"""
        return 2 * math.pi * self.__radius