#!/usr/bin/python3
"""NEW CLASS 3"""


class Square:
    """Square class.
    Args:
        size (int): size
    """
    def __init__(self, size=0):
        """ Init new square.
        Args:
            size (int): size in int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """ New method.
        """
    def area(self):
        return self.__size ** 2
