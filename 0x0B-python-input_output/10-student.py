#!/usr/bin/python3
"""the module doc"""


class Student:
    """The class student"""

    def __init__(self, first_name, last_name, age):
        """The constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the dict of the obj"""
        retu = []
        if all(type(item) == str for item in attrs):
            for key, value in self.__dict__.items():
                if key in attrs:
                    retu.append({key: value})
            return retu
        else:
            return self.__dict__
