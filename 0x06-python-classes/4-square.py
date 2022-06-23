#!/usr/bin/python3
""" defines a square template with a
    private attribute,
    property getter and setter for private field
    and a public method
"""


class Square:
    """ defines a
        *private instance attribute: size
        *property getter
        *property setter
        *public instance method
    """
    def __init__(self, size=0):
        """ instantiates an optional field
            Args:
                size(int): size of square
        """
        self.size = size

    @property
    def size(self):
        """ will retrieve and set the size private field of the square class
            Args:
                value is used to set the size attribute of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ compute the area of the square """
        return self.__size ** 2
