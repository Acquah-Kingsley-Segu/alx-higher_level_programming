#!/usr/bin/python3
""" defines a square template class
    with a private attribute and a validation feature
"""


class Square:
    """ Defines a square where its size id tested for validity """
    def __init__(self, size=0):
        """ Initializes a private size field with an optional size argument
            Arg:
                size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
