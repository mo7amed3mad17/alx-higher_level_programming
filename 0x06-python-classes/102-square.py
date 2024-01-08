#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """square."""

    def __init__(self, size=0):
        """Init a square.

        Args:
            size (int): The size
        """
        self.size = size

    @property
    def size(self):
        """Getter the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """The == comparision."""
        return self.area() == other.area()

    def __ne__(self, other):
        """The != comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """The < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """The <= comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """The > comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """The >= compmarison."""
        return self.area() >= other.area()
