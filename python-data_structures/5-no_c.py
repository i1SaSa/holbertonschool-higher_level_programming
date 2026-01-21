
def no_c(my_string):
    for i in my_string:
        y = ord(i)
        if y == 99 or y == 67:
            continue
        print("{}".format(chr(y)), end="")
    return chr(y)
