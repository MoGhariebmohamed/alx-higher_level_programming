#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    number = True
    try:
        print("{:d}".format(value))
    except Exception as E:
        print("Exception:", E, file=sys.stderr)
        number = False
    return number
