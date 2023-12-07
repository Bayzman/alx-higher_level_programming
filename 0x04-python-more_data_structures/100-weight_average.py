#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sums = 0
    weight = 0
    for val in my_list:
        sums += val[0] * val[1]
        weight += val[1]

    average = sums / weight

    return average
