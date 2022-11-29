#!/usr/bin/python3

def islower(c):
    chr_num = ord(c)

    if chr_num < 97 or chr_num > 122:
        print(False)
    else:
        print(True)
