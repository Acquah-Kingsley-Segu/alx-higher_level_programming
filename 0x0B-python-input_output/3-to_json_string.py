#!/usr/bin/python3
""" Convert python to json """


def to_json_string(my_obj):
    """ Convert content of an object into json
        Arg:
            * obj (python object): object to serialize into json
    """
    import json
    return json.dumps(my_obj)
