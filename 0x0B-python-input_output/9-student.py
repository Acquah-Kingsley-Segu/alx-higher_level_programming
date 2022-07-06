#!/usr/bin/python3
""" Module that hold a class definition """


class Student:
    """ Describe a student and has a public method
    """
    def __init__(self, first_name, last_name, age):
        """ Intantiate public instance classes
            Args:
                * first_name (str): student first name
                * last_name (str): student last name
                * age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dictionary representation of an object"""
        return self.__dict__
