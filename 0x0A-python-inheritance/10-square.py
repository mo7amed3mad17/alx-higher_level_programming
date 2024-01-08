#!/usr/bin/python3
"""Square  """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ Init Function """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area """
        return self.__size * self.__size
