#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(80):
        try:
            if i < a:
                raise Exception("too far")
            result = (a**b) / i
        except Exception:
            result = a+b
            break
        else:
            result = b+1
    return result
