#!/usr/bin/python3
'''
Docstring for python-input_output.7-add_item
'''
import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


load_from_json_file(add_item.json)
for i in sys.argv:
    save_to_json_file(i, add_item.json)
