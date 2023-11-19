#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = a_dictionary.copy()
    for mu in temp.keys():
        temp[mu] *= 2
    return (temp)
