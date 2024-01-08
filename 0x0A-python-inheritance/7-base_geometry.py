#!/usr/bin/python3
""" Improve Geometry """


class BaseGeometry:
    """ BaseGeometry """
    def area(self):
        """ Not yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validator """
        if type(value) is not int:
             raise TypeError("{} must be an integer".format(name))
        if value <= 0:
             raise ValueError("{} must be greater than 0".format(name))
