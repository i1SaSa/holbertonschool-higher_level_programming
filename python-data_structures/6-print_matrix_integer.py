#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        sep = ""
        for g in i:
            print(sep + "{:d}".format(g), end="")
            sep = " "
    print()
