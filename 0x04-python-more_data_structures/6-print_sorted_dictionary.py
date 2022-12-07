#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary={}):

    kys = list(a_dictionary.keys())
    kys.sort()

    for i in kys:
        print('{:s}: {}'.format(i,a_dictionary.get(i)))
