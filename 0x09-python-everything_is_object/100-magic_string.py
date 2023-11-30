#!/usr/bin/python3
def magic_string():
    magic_string.repeater = getattr(magic_string, "repeater", 0) + 1
    return (", ".join(["BestSchool" for x in range(magic_string.repeater)]))
