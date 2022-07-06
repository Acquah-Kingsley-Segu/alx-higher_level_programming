#!/usr/bin/python3
""" Returns a filtered dictionary description of a Student """


class Student:
    """ Provides a student template """
    def __init__(self, first_name, last_name, age):
        """ Instantiates public instance attributes
            Args:
                first_name (str): first name of student instance
                last_name (str): last_name of student instance
                age (int): age of student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return a filtered or full dictionary representation of an object
            attrs (list): used for the filtering feature
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            for item in attrs:
                if not isinstance(item, str):
                    return self.__dict__

        dict_des = {}
        for item in attrs:
            if item in self.__dict__:
                dict_des[item] = self.__dict__[item]
        return dict_des
