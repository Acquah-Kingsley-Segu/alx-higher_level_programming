#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = list(set(my_list))
    res = 0
    for num in unique:
        res += num
    return res
