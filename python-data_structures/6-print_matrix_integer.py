#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for f in matrix:
        for c in f:
            print("{:d}".format(c), end=" ")
        print()