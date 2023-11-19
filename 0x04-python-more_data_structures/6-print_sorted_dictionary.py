#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for it in sorted(a_dictionary):
        print("{:s}: {}".format(it, a_dictionary[it]))
