#!/usr/bin/python3

""" Read a text file (UTF8)
"""


def read_file(filename=""):
    """ Reads a text file
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
