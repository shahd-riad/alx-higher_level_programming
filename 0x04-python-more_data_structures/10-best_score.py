#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        scores = list(a_dictionary.values())
        scores.sort()
        for key in a_dictionary:
            if scores[-1] == a_dictionary[key]:
                return key
