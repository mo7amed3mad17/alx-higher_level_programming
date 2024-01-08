#!/usr/bin/python3
""" Define add integers function."""


def add_integer(a, b=98):
    """ Add 2 integers 
    Args:
        a (int/float): First num
        b (int/float): Second num
    Raises:
        TypeError: if a either is not int nor float
        TypeError: id b either is not int nor float
    Returns:
        The result of adding a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
