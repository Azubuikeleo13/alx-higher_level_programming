#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    kys = sorted(a_dictionary)
    kys.sort()

    for i in kys:
        print('{:s}: {}'.format(i, a_dictionary.get(i)))
