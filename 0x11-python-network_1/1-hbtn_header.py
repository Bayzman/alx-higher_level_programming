#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays \
    the value of the X-Request-Id variable found in the \
    header of the response.
"""

import urllib
from sys import argv


def main():
    """ Main function """
    url = argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
