#!/usr/bin/python3
""" Does matrix element-wise division """


def matrix_divided(matrix, div):
    list_len = 0
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if list_len == 0:
            list_len = len(row)
        if len(row) != list_len:
            raise TypeError("Each row of matrix must have the same size")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(num / div, 2) for num in row] for row in matrix]
