#!/usr/bin/python3
print("".format()
        .join([chr(a) for a in range(ord('a'), ord('z')+1)
        if a == 'q' or a == 'e':
            a = ""]), end="")
