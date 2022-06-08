#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_sorted = sorted(list(a_dictionary.keys()))
    for key in key_sorted:
        print("{}: {}".format(key, a_dictionary[key]))
