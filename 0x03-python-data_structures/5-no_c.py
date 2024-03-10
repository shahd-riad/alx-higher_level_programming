#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    while 'c' in mylist:
        mylist.remove('c')
    while 'C' in mylist:
        mylist.remove('C')
    newString = ''.join(mylist)
    return newString
