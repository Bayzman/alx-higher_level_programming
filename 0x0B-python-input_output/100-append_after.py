#!/usr/bin/python3

""" A function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file after each line after
        each line containing a specific string
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)
        else:
            continue

    with open(filename, 'w') as file:
        file.writelines(new_lines)
