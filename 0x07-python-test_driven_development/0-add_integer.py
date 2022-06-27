#!/usr/bin/python3
""" 
This is the ``0-add_integer`` module.

The module has one function that return sum of it parameters
"""

def add_integer(a, b=98):
    """ return int(a) + int(b) 
        Args: a: position number argument || b: optional number argument
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if not a:
        raise TypeError("at least one argument should be passed to ``add_integer``")
    return int(a) + int(b)
