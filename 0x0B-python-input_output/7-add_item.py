#!/usr/bin/python3
"""this module Write a function adds all arguments to a Python list,"""

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    lis_item = load_from_json_file("add_item.json")
except FileNotFoundError:
    lis_item = []
    lis_item.extend(sys.argv[1:])
    save_to_json_file(lis_item, "add_item.json")
