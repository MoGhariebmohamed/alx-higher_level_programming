#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda E: replace if E == search else E, my_list))
