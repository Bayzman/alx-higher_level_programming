#!/usr/bin/python3

""" Prints a text with 2 new lines after each of these characters: ., ? and : """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    characters = ['.', '?', ':']

    for i in characters:
        text = text.replace(i, i + '\n')

    lines = text.split('\n')
    count = 0

    for line in lines:
        # Remove whitespaces at the beginning and end of each line
        strip_line = line.strip()
        count += 1

        # Ensure no new line character is added after the last line
        if (strip_line and count < len(lines)):
            print(strip_line + '\n')
        else:
            print(strip_line, end='')
