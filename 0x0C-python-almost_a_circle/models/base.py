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
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs == [] or list_objs is None:
            wr = []
        else:
            ty = type(list_objs[0])
            if any(type(i) != ty for i in list_objs):
                raise ValueError("all elements of list_objs must match")
            wr = [i.to_dictionary() for i in list_objs]
        fname = cls.__name__+".json"
        with open(fname, "w") as f:
            content = cls.to_json_string(wr)
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """to the string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """second class method"""
        dummy = cls(2, 3) if cls.__name__ == "Rectangle" else cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load"""
        the_load = ""
        try:
            with open(cls.__name__+".json") as f:
                the_load = f.read()
        except Exception as e:
            return []
        ins = cls.from_json_string(the_load)
        return cls.create(ins)
