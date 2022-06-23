#!/usr/bin/python3
""" defines a square class template with a
    private instance field, a
    property getter and setter method and
    two public methods
"""


class Square:
    """ the square template with a private field """
    def __init__(self, size=0):
        """ the intializer method for the square class
            Args:
                size (int): the size of the square object instance
        """
        self.size = size

    @property
    def size(self):
        """ the property decorator to take on the getter and setter
            * for the getter method: returns the size private field of instance
            * for the setter method:
                Args:
                    value (int): size to be instatiated for the object
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
        """ computes the area of the given instance """
        return self.__size ** 2

    def my_print(self):
        """ prints the square using the '#' symbol to stdout """
        for num in range(1, self.area() + 1):
            if num % self.__size == 0:
                print("#")
            else:
                print("#", end="")
