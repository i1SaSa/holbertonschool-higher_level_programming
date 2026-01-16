#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        x = a
        for i in range(b - 1):
            a *= x
    else:
        x = a
        for i in range(b - 1):
            a *= x
        return 1/a
    return a
