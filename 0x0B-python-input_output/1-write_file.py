#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ Write content of text to file specified in filename
        Args:
            * filename (str): name or path of file
            * text (str): content to write to file
    """
    with open(filename, 'w', encoding='utf-8') as fname:
        written_len = fname.write(text)
    return written_len
