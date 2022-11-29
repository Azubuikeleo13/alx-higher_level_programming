#!/usr/bin/python3

def islower(c):

    chr_num = ord(c)

    if chr_num > 96 and chr_num < 123:
        return True
    else:
        return False
