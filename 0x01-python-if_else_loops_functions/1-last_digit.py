#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    LastDigit = number % 10
else:
    LastDigit = ((number * -1) % 10) * -1
info = "Last digit of %d is %d and is" % (number, LastDigit)
if LastDigit == 0:
    print(info, "0")
elif LastDigit > 5:
    print(info, "greater than 5")
else:
    print(info, "less than 6 and not 0")

