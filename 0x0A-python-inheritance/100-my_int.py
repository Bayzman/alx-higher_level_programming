#!/usr/bin/python3
''' MyInt class is a rebel that inherits from the int class '''


class MyInt(int):
    ''' MyInt inverts == and != '''

    def __eq__(self, val):
        ''' Inverts == '''

        return (self - val != 0)

    def __ne__(self, val):
        ''' Inverts != '''

        return (self - val == 0)
