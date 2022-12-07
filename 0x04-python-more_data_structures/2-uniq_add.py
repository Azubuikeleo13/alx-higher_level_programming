#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq = []

    for i in my_list:
        if i in uniq:
            continue

        uniq.append(i)

    summ = sum(uniq)
    return summ
