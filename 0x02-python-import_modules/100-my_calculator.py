#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv
    operator = "+-*/"
    argv_len = len(argv) - 1
    print(argv_len)
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
                print("{} {} {} = {}".format(a, op, b, cal.add(a, b)))
            elif op == '-':
                print("{} {} {} = {}".format(a, op, b, cal.sub(a, b)))
            elif op == '*':
                print("{} {} {} = {}".format(a, op, b, cal.mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, op, b, cal.div(a, b)))
            exit(0)
