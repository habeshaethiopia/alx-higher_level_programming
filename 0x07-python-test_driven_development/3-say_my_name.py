#!/usr/bin/python3
""" THE module that prints ma name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """ A method to say my name"""
    if type(first_name) != str:
        raise TypeError(
            "first_name must be a string or last_name must be a string")
    if type(last_name) != str:
        raise TypeError(
            "last_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
