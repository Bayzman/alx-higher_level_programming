#!/usr/bin/python3

""" Adds all arguments to a Python list, and then save them to a file
"""
import json
import sys
import os.path


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.isfile(filename):
    out = load_json(filename)

else:
    out = []

out.extend(sys.argv[1:])
save_json(out, filename)
