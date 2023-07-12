#!/usr/bin/python3
"""the module doc"""


def append_write(filename="", text=""):
    """the function doc"""
    with open(filename, "a") as f:
        return f.write(text)
