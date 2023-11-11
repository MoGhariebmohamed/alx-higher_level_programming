#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for x in range(len(my_list)):
        if my_list[x] == search:
            my_list[x] = replace
            new_list.append(my_list[x])
        else:
            new_list.append(my_list[x])
    return new_list
