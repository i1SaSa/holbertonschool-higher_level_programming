#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print("\n")
        for g in i:
            print("{:d}".format(g), end=" ")
