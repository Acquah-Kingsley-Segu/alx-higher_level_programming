#!/usr/bin/python3
""" Prints text with newlines """


def text_indentation(text):
    """ Prints a new version of a string by
        replaing (., ? and :) with two newline (\\n)
        Arg:
            text (str): string to be transformed
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print(f"{char}\n")
        else:
            print(char, end="")
