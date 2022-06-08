#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    largest = ['', 0]
    for key, value in a_dictionary.items():
        if value >= largest[1]:
            largest[0] = key
            largest[1] = value
    return largest[0]
