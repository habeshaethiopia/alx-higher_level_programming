#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = abs(number) % 10 * -1
print("Last digit of {} is {} ".format(number, last), end="")
if last > 5:
    print("and greater than 5")
elif last == 0:
    print("and equal to 0")
elif last < 6:
    print("and less than 6")
