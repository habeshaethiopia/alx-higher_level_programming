#!/usr/bin/python3
"""module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """squre class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the string Notation"""
        return "[Square] ("+str(self.id) + ") "+str(self.x) +\
            "/"+str(self.y)+" - "+str(super().width)
