#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = ord(x) - 32
            x = chr(x)
        print('{}'.format(x), end="")
    print()
