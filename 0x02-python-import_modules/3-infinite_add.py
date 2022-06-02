#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv
    len_args = len(args) - 1
    add = 0
    if len_args == 0 or len_args == 1:
        print("{}".format(len_args))
    else:
        for index in range(1, len_args + 1):
            add += int(args[index])
        print("{}".format(add))
