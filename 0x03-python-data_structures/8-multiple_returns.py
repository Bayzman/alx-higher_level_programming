#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        length = 0
        first = None
        print("Length: {} - First character: {}".format(length, first))

    length = len(sentence)
    first = sentence[0]
    print("Length: {} - First character: {}".format(length, first))
