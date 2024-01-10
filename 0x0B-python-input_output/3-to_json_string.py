#!/usr/bin/python3
''' Returns the JSON representation of an object (string) '''
import json


def to_json_string(my_obj):
    ''' Returns the JSON representation

    Args:
        my_obj (str): string

    Return:
        json object
    '''

    return json.dumps(my_obj)
