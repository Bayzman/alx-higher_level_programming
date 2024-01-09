#!/usr/bin/python3
''' Inherits from list
'''


class MyList(list):
    ''' MyList inherists from list
    '''

    def print_sorted(self) -> None:
        ''' Prints sorted list in ascending order '''

        print(sorted(self))
