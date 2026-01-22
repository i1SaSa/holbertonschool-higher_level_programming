#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    y = 0
    for i in my_list:
        if i > y:
            y = i
        elif y >= 0 >= i:
            y = i
    return y
