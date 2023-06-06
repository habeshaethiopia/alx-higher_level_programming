#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number:d} is ")
if number > 0:
    last = number % 10
else:
    last = abs(number) % 10 * -1
if last > 5:
    print(f"{l:d} and greater than 5")
elif last == 0:
    print(f"{l:d} and equal to 0")
elif last < 6:
    print(f"{l:d} and less than 6")
