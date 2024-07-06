#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the body of
    the response (decoded in utf-8).
"""
from sys import argv
from urllib import error
from urllib.request import Request, urlopen


def main():
    try:
        with urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
