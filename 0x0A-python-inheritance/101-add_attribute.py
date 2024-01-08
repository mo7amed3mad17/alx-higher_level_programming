#!/usr/bin/python3
"""Add Atributte """


def add_attribute(obj, att, value):
    """Add a new attribute

    Args:
        obj (any): The object
        att (str): The name of the attribute
        value (any): The attr value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

