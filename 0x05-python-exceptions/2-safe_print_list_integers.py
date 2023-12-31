#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    temp = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            temp += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (temp)
