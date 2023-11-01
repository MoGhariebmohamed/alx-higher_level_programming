#!/usr/bin/python3
def print_last_digit(number):
    N = abs(number) % 10
    print("{}".format(N), end="")
    return N
