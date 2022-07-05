#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    written_len = 0
    for char in text:
        written_len += 1
    with open(filename, 'w', encoding='utf-8') as fname:
        fname.write(text)
    return written_len
