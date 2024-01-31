#!/usr/bin/python3
def uniq_add(my_list=[]):
    lituple = set(my_list)
    sum = 0
    for element in list(lituple):
        sum += element
    return sum
