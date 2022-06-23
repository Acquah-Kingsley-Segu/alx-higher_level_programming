#!/usr/bin/python3
""" module defines a square template class with two
    private instance field attribute,
    property getters and setters, and two
    public instance methods
"""


class Square:
    """ create the square class template """

    def __init__(self, size=0, position=(0, 0)):
        """ instantiate two private instance fields
            Args:
            size (int): the dimension of the square
            position (tuple): position in terms of x-y coordinate
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ property getter-setter definition
            Getter: return the size of square
            Setter: sets the size of the square
                Arg:
                    value (int): variable to be use to set square size
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

    @property
    def position(self):
        """ property getter-setter definition
            Getter: returns the coordinate position of square to be drawn
            Setter: sets the coordinate of the square
                Arg:
                    value (tuple): coordinate to use to set position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
           (len(value) != 2) or
           (not (isinstance(value[0], int) and isinstance(value[1], int))) or
           (value[0] < 0 and value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ computes the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints the square produced by area at the specified position """
        space = 0
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print()
            for num in range(1, self.area() + 1):
                if self.__position[0] > 0 and not space:
                    for x in range(self.__position[0]):
                        print(" ", end="")
                if num % self.__size == 0:
                    print("#")
                    space = 0
                else:
                    space = 1
                    print("#", end="")
