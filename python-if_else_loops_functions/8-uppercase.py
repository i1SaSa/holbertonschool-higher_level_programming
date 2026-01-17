#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if 97 <= c <= 122:
            c = c - 32
        print("{}".format(chr(c)), end="")
    print("")
