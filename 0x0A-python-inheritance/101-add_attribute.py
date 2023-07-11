#!/usr/bin/python3
"""module document"""


def add_attribute(object, attribute, value):
    """adds a new attribute"""
    if not hasattr(object, "__slots__") and not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(object, "__slots__") and not hasattr(object, attribute):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
