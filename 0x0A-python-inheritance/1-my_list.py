#!/usr/bin/python3
"""Module contain MyList class"""


class MyList(list):
    """the class"""

    def print_sorted(self):
        """To sort the list"""
        print(sorted(self))
