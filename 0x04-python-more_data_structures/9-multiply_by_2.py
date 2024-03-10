#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    for key in a_dictionary:
        newDict[key] = 2 * a_dictionary[key]
    return newDict
