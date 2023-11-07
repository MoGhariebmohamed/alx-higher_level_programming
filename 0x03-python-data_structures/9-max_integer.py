#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        sortlist = sorted(my_list)
        max_list = sortlist[-1]
        return (max_list)
