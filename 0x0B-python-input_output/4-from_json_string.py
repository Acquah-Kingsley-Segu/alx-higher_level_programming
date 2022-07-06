#!/usr/bin/python3
""" JSON string ---> Python Object """


def from_json_string(my_str):
    """ Change json string into python object and return it
        Arg:
            my_str (json string): json string to convert
    """
    import json
    return json.loads(my_str)
