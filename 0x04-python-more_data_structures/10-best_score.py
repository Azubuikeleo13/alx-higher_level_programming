#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return

    bst = 0

    for i in a_dictionary.keys():
        if a_dictionary.get(i) > bst:
            bst = a_dictionary.get(i)
            nam = i

    return nam
