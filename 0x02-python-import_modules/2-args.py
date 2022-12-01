#!/usr/bin/python3

import sys

no_arg = len(sys.argv) - 1

if no_arg == 0:
    print('{} arguments.'.format(no_arg))
else:
    print('{} arguments:'.format(no_arg))

    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
