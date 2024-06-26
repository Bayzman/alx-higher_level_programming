#!/usr/bin/python3

""" Writes an object to a text file, using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file, using a JSON representation

    Args:
        my_obj (str): object
        filename (str): file name
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
