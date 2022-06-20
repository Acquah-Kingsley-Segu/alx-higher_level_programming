#!/usr/bbin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (TypeError, ValueError):
            continue
        else:
            counter += 1
    print()
    return counter
