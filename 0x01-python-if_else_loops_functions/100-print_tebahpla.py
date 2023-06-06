#!/usr/bin/python3
for a in range(-ord('z'), -ord('a')+1):
    if a % 2 == 0:
        f = 0
    else:
        f = 32
    print("{}".format(chr(-1*a - f)), end="")
