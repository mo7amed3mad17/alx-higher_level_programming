#!/usr/bin/python3
""" Exact Same Object. """


def is_same_class(obj, a_class):
    """ Return True or False. """
    if type(obj) is a_class:
        return True
    else:
        return False
