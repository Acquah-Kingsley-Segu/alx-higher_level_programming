#!/usr/bin/python3
""" Defines a rectangle by:
     * two private instance attribute
     * and property/property setter for both
"""


class Rectangle:
    """A rectangle template with private dimensions"""
    def __init__(self, width=0, height=0):
        """ Makes instance properties of an instance ready for use
            Args:
                width (int): width dimension of rectangle
                height (int): height dimension of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property getter and setter definition
            Getter: return the width
            Setter: sets the width of the rectangle
                Arg:
                 value (int): used to instantiate width dimension of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Property getter and setter definition
            Getter: return the height
            Setter: sets the height of the rectangle
                Arg:
                 value (int): used to instantiate width dimension of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
