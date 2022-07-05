#!/usr/bin/python3
""" Append content to file """


def append_write(filename="", text=""):
    """ Appends the content of text to filename
        Args:
            filename (str): name of file or path to file
            text (str): content to append
    """
    with open(filename, 'a', encoding='utf-8') as fname:
        char = fname.write(text)
    return char
