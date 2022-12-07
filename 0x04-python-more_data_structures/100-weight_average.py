#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list is []:
        return 0

    new_ls = []

    for i in my_list:
        prd = 1

        for j in i:
            prd *= j

        new_ls.append(prd)

    summ = sum(new_ls)
    wei = 0

    for i in my_list:
        for j in range(1, len(i)):
            wei += i[j]

    aver = float(summ / wei)

    return aver
