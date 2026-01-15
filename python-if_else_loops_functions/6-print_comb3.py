#!/usr/bin/python3
x = 0
for i in range(10):
    x += 1
    for j in range(x, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
