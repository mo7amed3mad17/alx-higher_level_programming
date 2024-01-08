#!/usr/bin/python3
""" New Rec """


class Rectangle:
    """ New Rec Class """
    def __init__(self, width=0, height=0):
        """ Init New Rec
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width
          Args:
              value (int): width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height
          Args:
              value (int): height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Return the printable rectangle.
           rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """ The string rectangle."""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Print a deletion messege."""
        print("Bye rectangle...")
