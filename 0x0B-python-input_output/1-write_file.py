#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as fname:
        written_len = fname.write(text)
    return written_len
