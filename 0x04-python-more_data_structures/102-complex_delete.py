#!/usr/bin/python3
def complex_delete(a_dict, value):
    new_dict = a_dict.copy()
    for key, val in new_dict.items():
        if (value == val):
            del a_dict[key]

    return a_dict
