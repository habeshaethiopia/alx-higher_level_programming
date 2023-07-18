#!/usr/bin/python3

"""this is the module contain Bse class"""

import json


class Base:
    """doc for this calss"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the class constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(i) != dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to the file"""
        if not isinstance(cls, list_objs):
            raise TypeError("list_objs must be sub class of Base")
        with open(str(cls)+".json", "w") as f:
            res = to_json_string(list_objs)
            f.write(res)
