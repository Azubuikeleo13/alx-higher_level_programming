#!/usr/bin/python3

def islower(c):
    chr_num = ord(c)

    if chr_num < 97 and chr_num > 122:
        return False
    else:
        return True
