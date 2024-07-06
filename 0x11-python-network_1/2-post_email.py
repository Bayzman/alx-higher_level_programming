#!/usr/bin/python3

""" takes in a URL and an email, sends a POST request """

from sys import argv
from urllib import request, parse


def main():
    """ Main function
    """
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    content = parse.urlencode(values)

    request = request.Request(url, content.encode('ascii'))
    with request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    main()
