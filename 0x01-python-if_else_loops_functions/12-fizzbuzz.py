#!/usr/bin/python3
def fizzbuzz():
    Y = range(1, 101)
    for X in Y:
        if X % 3 == 0 and X % 5 != 0:
            print("Fizz ", end="")
        elif X % 5 == 0 and X % 3 != 0:
            print("Buzz ", end="")
        elif X % 5 == 0 and X % 3 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ".format(X), end="")
