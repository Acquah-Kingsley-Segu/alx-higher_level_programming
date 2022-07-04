#!/usr/bin/python3
""" Checks if object is an instance """


def is_same_class(obj, a_class):
    """ Prints the boolean value after instance check is done
        Args:
            obj (class_instance): object whose instance is to be checked
            a_class (class): class to check object against
    """
    return isinstance(obj, a_class)
