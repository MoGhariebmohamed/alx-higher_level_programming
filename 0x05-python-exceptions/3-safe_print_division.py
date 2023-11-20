#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        y = a / b
    except (TypeError, ZeroDivisionError):
        y = None
    finally:
        print("Inside result: {}".format(y))
    return (y)
