#!/usr/bin/python3
"""the module doc"""


def read_file(filename=""):
    """function doc"""
    with open(filename) as f:
        for line in f:
            print(line)
