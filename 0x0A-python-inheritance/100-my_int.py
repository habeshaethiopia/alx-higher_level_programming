#!/usr/bin/python3
"""MOdule documentation"""


class MyInt(int):
    """myint class"""

    def __eq__(self, other):
        """function documented"""
        return super().__ne__(other)

    def __ne__(self, other):
        """function documented"""
        return super().__eq__(other)
