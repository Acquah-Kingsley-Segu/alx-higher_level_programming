#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for item in my_list:
        if counter >= x:
            break
        print(item, end="")
        counter += 1
    print()
    return counter