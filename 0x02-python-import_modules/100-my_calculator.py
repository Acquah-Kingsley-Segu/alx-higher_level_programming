#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    operator = "+-*/"
    argv_len = len(argv) - 1
    if argv_len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if op == '+':
                print("{} {} {} = {}".format(a, op, b, add(a, b)))
            elif op == '-':
                print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            elif op == '*':
                print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, op, b, div(a, b)))
            exit(0)
