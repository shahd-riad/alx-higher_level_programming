#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == 0:
        firstL = 'None'
    else:
        firstL = sentence[0]
    return length, firstL
