#!/usr/bin/python3
""" Defines a rectangle by:
     * two private instance attribute
     * and property/property setter for both
    and finds the:
     * area
     * perimeter
     * largest rectangle
    using public instance methods
"""


class Rectangle:
    """A rectangle template with
        * private dimensions
        * public class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Makes instance properties of an instance ready for use
            Args:
                width (int): width dimension of rectangle
                height (int): height dimension of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size = 0):
        return (Rectangle(size, size))

    def __del__(self):
        """Sees to that instance deletion goes smoothly"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return perimeter of the rectangle"""
        if self.__width > 0 and self.__height > 0:
            return ((2 * self.__width) + (2 * self.__height))
        return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Prints the rectangle using #-symbol"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for num in range(1, self.__height + 1):
                rectangle += self.__width * str(self.print_symbol)
                if num < self.__height:
                    rectangle += "\n"
        return rectangle

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
