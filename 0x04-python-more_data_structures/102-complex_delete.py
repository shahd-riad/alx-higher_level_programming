#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    sortin = list(a_dictionary.keys())
    for value_dic in sortin:
        if a_dictionary[value_dic] == value:
            del a_dictionary[value_dic]
    return (a_dictionary)
