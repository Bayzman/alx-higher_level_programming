#!/usr/bin/python3

""" fetches https://alx-intranet.hbtn.io/status """
import requests


def main():
    """ Main function """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
