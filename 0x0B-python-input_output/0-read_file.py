#!/usr/bin/python3
""" Read a file content """


def read_file(filename=""):
    """ Prints the content of a file to stdout
        Arg:
            filename (str): name or path of file
    """
    with open(filename, encoding='utf-8') as fname:
        for line in fname:
            print(line, end="")
