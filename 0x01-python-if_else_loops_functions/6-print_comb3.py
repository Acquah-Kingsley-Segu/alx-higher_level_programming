#!/usr/bin/python3

for num in range(9):
    for num2 in range(num+1, 10):
        if num != 8 or num2 != 9:
            print("{}{}".format(num, num2), end=", ")
        else:
            print("{}{}".format(num, num2))
