#!/usr/bin/python3

""" takes 2 arguments in order to solve this challenge
"""
from sys import argv
import requests


def main():
    """ Main Function
    """
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".
                  format(commits[i]['sha'],
                         commits[i]['commit']['author']['name']))
    except IndexError:
        pass


if __name__ == "__main__":
    main()
