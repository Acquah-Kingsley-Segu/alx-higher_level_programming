#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        lst = []
        for num in row:
            lst.append(num ** 2)
        new_matrix.append(lst)
    return(new_matrix)
