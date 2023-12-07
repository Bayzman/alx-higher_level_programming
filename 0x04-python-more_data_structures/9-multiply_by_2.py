#!/usr/bin/python3
def multipy_by_2(a_dictionary):
    # new_dict = {}
    for key, value in a_dictionary.items():
        a_dictionary[key] = value * 2

    return a_dictionary
