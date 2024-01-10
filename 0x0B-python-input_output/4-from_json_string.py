#!/usr/bin/python3
''' Returns an object (Python data structure) represented by a JSON string
'''
import json


def from_json_string(my_str):
    ''' Convert JSON to Python data structure (object)

    Args:
        my_str (str): JSON string representation

    Return:
        my_str (json): JSON string
    '''

    return json.loads(my_str)
