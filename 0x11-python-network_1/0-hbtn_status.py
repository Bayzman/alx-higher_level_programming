#!/usr/bin/python3

""" fetches https://alx-intranet.hbtn.io/status """
from urllib.request import Request, urlopen


def main():
    """ Main function """

    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))


if __name__ == '__main__':
    main()
