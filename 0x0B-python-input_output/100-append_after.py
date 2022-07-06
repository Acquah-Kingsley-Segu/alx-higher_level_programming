#!/usr/bin/python3
""" Append to file """


def append_after(filename="", search_string="", new_string=""):
    """ Appends a string to a file if search was successful
        Args:
            filename (str): path of file
            search_strings (str): search item
            new_string (str): string to append after sucessful search
    """
    content = []
    with open(filename, encoding="utf-8") as fname:
        for line in fname:
            content.append(line)
            if line.find(search_string) >= 0:
                content.append(new_string)

    with open(filename, "w", encoding="utf") as fname:
        fname.writelines(content)
