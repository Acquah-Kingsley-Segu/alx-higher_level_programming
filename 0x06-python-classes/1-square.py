#!/usr/bin/python3
""" defines a square template class with a private atrribute """


class Square:
    """Defines a square"""
    def __init__(self, size):
        """ Instatiate the attributes for fields
            Args:
                size (int): represents the size of the square
        """
        self.__size = size
