#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortin = list(a_dictionary.keys())
    sortin.sort()
    for key in sortin:
        print("{}: {}".format(key, a_dictionary[key]))
