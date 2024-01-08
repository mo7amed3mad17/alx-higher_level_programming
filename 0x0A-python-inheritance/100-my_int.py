#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """Class My int"""

    def __eq__(self, value):
        """__eq__"""
        return self.real != value

    def __ne__(self, value):
        """__ne__"""
        return self.real == value
