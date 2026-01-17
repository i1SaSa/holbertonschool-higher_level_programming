#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = 0
    if (len(sys.argv) - 1) == 0:
        print(0)
    else:
        for i in sys.argv[1:]:
            x += int(i)
        print(x)
