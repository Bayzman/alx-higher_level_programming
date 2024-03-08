#!/usr/bin/python3
""" prints a text with 2 new lines after each of these
    characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these
        characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    characters = ['.', '?', ':']

    for i in characters:
        text = text.replace(i + '', i + '\n')

    lines = text.split('\n')

    count = 0

    for line in lines:
        strip_line = line.strip()
        count += 1
        if (strip_line and count < len(lines)):
            print(strip_line)
            print()
        else:
            print(strip_line, end='')
