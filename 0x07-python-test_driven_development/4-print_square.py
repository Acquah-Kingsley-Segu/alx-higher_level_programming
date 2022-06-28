#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """ Prints a square with the #-symbol based on its area
        Arg:
            size (int): the size of square dimension
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    for num in range(1, size+1):
        print(size * "#", end="")
        print()
