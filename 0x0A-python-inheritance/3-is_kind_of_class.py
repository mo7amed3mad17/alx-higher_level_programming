#!/usr/bin/python3
""" Same Class Or Inherit From """


def is_kind_of_class(obj, a_class):
    """ Return True or False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
