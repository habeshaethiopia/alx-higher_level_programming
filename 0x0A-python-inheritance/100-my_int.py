#!/usr/bin/python3
"""MOdule documentation"""


class MyInt(int):
    """myint class"""

    def __init__(self,  val):
        """initilizer"""
        self.val = val

    def __eq__(self, other):
        """function documented"""
        return self.val != other.val

    def __ne__(self, other):
        """function documented"""
        return self.val == other.val
