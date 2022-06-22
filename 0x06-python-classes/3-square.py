#!/usr/bin/python3
class Square:
    """ A square that is able to calculate its area """
    def __init__(self, size=0):
        """ validates the size argument passed to class
            Arg:
                size (int): an optional size value of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the area of the caller square object(self)
            Args:
                has no argument passed to it
            Returns:
                area of the object square
        """
        return self.__size ** 2
