#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    for i in my_list[x::-1]:
        print("{:d}".format(i))
        x -= 1
