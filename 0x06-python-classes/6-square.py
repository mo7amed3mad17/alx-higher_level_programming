#!/usr/bin/python3
""" NEW CLASS. """


class Square:
    """Square class.
    Args:
        size (int): size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init new square.
        Args:
            size (int): size
            position (int, int): position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ return size
        """
        return self.__size

    @property
    def position(self):
        """Getter position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """Setter position.
        Args:
            value (int): size
        """
        if type(value) is not tuple or len(value) != 2 \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return area
        """
        return self.__size ** 2

    def my_print(self):
        """ Print squares
        """
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print("")
        for j in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for m in range(0, self.__size):
                print("#", end="")
            print("")
