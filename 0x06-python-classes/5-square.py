#!/usr/bin/python3
""" NEW CLASS. """


class Square:
    """Square class.
    Args:
        size (int): size
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size
          Args:
              value (int): size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area
        """
        return self.__size ** 2

    def my_print(self):
        """ Print squares
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
