#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
num1 = str(number)
num2 = num1[-1]
num3 = int(num2)

if number < 0:
    num3 *= -1

if num3 > 5:
    print(f'Last digit of {number:d} is {num3:d} and is greater than 5')
elif num3 < 6 and num3 != 0:
    print(f'Last digit of {number:d} is {num3:d} and is less than 6 and not 0')
else:
    print(f'Last digit of {number:d} is {num3:d} and is 0')
