#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for f in matrix:
        for c in f:
            if c != f[-1]:
                print("{:d}".format(c), end=" ")
            else:
                print("{:d}".format(c))
