#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value
    of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


def main():
    """ Main function """
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
