#!/usr/bin/python3
""" Create object from json file content """


def load_from_json_file(filename):
    import json
    """ creates an object from a json string stored in a file
        arg:
            filename (str): file to read json object from
    """

    with open(filename, encoding='utf-8') as fname:
        return json.load(fname)
