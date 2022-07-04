#!/usr/bin/python3
""" Module that shows the members of an object """


def lookup(obj):
    """ Returns a list of attributes and methods of an object
        Arg:
            obj (class instance): object to be used
    """
    return (dir(obj))
