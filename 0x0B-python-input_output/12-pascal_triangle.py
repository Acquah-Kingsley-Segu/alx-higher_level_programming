#!/usr/bin/python3
""" Module with function that perform pascal triangle """


def pascal_triangle(n):
    """ Perform pascal triangle from 0 to n.
        It then returns a list of lists
        Arg:
            * n (int): maximum pascal term 
                       ie. from 0 ---> (n - 1)th term
    """

    if n <= 0:
        return []
    row_list = []
    pascal = []
    for row in range(n):
        for col in range(row+1):
            if col == 0 or col == row:
                row_list.append(1)
            else:
                row_list.append(pascal[row-1][col-1] + pascal[row-1][col])
        pascal.append(row_list)
        row_list = []
    return pascal
