#!/usr/bin/python3
for i in range(100):
    print("{}".format(i // 10), end="")
    if i != 99:
        print("{}, ".format(i % 10), end="")
    else:
        print("{} ".format(i % 10))
