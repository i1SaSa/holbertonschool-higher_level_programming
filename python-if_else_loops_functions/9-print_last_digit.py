#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return print(10 - (number % 10), end="")
    return print(number % 10, end="")
