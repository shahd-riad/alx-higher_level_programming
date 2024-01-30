#!/usr/bin/python3
a = 89
b = 10
tupleq = a , b
b , a = tupleq
print("a={:d} - b={:d}".format(a, b))
