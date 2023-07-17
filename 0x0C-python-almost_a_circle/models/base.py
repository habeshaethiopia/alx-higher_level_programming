#!/usr/bin/python3

"""this is the module contain Bse class"""


class Base:
    """doc for this calss"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the class constractor"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
