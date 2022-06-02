#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv
    len_args = len(args) - 1
    if len_args == 1:
        print("{} argument:".format(len_args))
    else:
        print("{} arguments".format(len_args), end = "")
        if len_args == 0:
            print(".")
        else:
            print(":")
    if len_args > 0:
        for index in range(1, len_args + 1):
            print("{}: {}".format(index, args[index]))
