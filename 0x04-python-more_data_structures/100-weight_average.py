#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    upper = 0
    lower = 0
    for tup in my_list:
        num1, num2 = tup
        upper += (num1 * num2)
        lower += num2
    return upper/lower
