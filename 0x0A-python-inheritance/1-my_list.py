#!/usr/bin/python3
""" Inherits from list."""


class MyList(list):
    """ MyList class. """
    def print_sorted(self):
        """ Print sorted elements of list. """
        print(sorted(self))
    
