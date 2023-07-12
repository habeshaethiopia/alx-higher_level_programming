#!/usr/bin/python3
"""the module doc"""


def write_file(filename="", text=""):
    """function doc"""
    with open(filename, "w") as f:
        return f.write(text)
