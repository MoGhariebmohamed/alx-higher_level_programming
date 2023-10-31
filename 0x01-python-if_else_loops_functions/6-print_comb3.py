#!/usr/bin/python3
for X in range(0, 9):
    for Y in range(X +1, 10):
        if X == 8 and Y == 9:
            print("{:d}{:d}".format(X,Y))
        else:
            print("{:d}{:d}, ".format(X,Y), end="")
