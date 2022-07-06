#!/usr/bin/python3
""" saving json object """


def save_to_json_file(my_obj, filename):
    """ Will save json string to a file
        Args:
            * my_obj (object): object to serialize
            * filename (str): file path to store serialized json data
    """
    import json

    with open(filename, 'w', encoding='utf-8') as fname:
        json.dump(my_obj, fname)
