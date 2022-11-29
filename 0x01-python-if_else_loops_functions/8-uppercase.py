#!/usr/bin/python3

def uppercase(str):

    for i in str:
        str_num = ord(i)

        if str_num > 96 and str_num < 123:
            str_num -= 32

        str_chr = chr(str_num)
        print('{}'.format(str_chr), end='')

    print('')
