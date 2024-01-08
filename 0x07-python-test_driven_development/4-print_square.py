#!/usr/bin/python3
""" Define Squares printer function."""


def print_square(size):
    """ Print Squares with the sign (#)

    Args:
        size (int): The length of the square
    Raises:
        TypeError: if size is not int, or if size is float and less than 0
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for ele in range(size):
            print("#", end="")
        print()
