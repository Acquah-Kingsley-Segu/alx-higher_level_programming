#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = my_list[0]
    for idx in range(1, len(my_list)):
        if my_list[idx] > largest:
            largest = my_list[idx]
    return largest
