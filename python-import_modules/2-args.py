#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = 0
    y = 0
    for u in sys.argv[1:]:
        y += 1
    if len(sys.argv) > 1:
        print("{} arguments:".format(y))
    else:
        print("0 arguments.")

    for i in sys.argv[1:]:
        x += 1
        print("{}: {}".format(x, i))
