#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    no_arg = len(sys.argv) - 1
    summ = 0

    if no_arg == 0:
        print('{}.'.format(summ))
    else:
        for i in range(1, len(sys.argv)):
            summ += int(sys.argv[i])
        print(summ)
