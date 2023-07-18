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
            "/"+str(self.y)+" - "+str(self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """afunction update"""
        if args is not None:
            if len(args) > 0:
                if args[0]:
                    self.id = args[0]
            if len(args) > 1:
                if args[1]:
                    self.size = args[1]
            if len(args) > 2:
                if args[2]:
                    self.x = args[2]
            if len(args) > 3:
                if args[3]:
                    self.y = args[3]
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """make the dictionary"""
        dic = {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
        return dic
