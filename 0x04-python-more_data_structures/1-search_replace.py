#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list

    Args:
        my_list (list): original list
        search (any): element of any data type
        replace (any): element of any data type

    Returns:
        list: new list
    """

    new_list = my_list.copy()
    for i in range(len(new_list)):
        if (new_list[i] == search):
            new_list[i] = replace

    return new_list
