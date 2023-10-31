#!/usr/bin/python3
for H in range(0, 100):
    if H == 99:
        print(H)
    else:
        print("{:02}, ".format(H), end="")
