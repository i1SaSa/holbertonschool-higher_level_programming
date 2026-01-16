#!/usr/bin/python3
def pow(a, b):
    x = a
    for i in range(b - 1):
        a *= x
    return a
