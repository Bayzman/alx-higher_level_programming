#!/usr/bin/python3

""" Inherit from list and prints a sorted list """


class MyList(list):
    """ Inherit from list and prints a sorted list """

    def print_sorted(self):
        """ prints a sorted list """

        new_list = sorted(self)
        print(new_list)

        return new_list
