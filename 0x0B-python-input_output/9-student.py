#!/usr/bin/python3
"""the module doc"""


class Student:
    """The class student"""

    def __init__(self, first_name, last_name, age):
        """The constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """the dict of the obj"""
        return self.__dict__
