#!/usr/bin/python3
def pow(a, b):
    x = a
    if b > 0:
        for i in range(b - 1):
            a *= x
        return a
    else:
        for i in range(0, b + 1, -1):
            a *= x
        return 1/a
    return a
