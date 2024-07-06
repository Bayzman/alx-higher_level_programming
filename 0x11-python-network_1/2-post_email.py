#!/usr/bin/python3

""" takes in a URL and an email, sends a POST request """
from sys import argv
import urllib.parse
from urllib.request import Request, urlopen


def main():
    """ Main function """
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    content = urllib.parse.urlencode(values)
    req = Request(url, content.encode('ascii'))
    with urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    main()
