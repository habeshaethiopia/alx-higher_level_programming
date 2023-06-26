#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if notisdigit(value):
            raise Exception
        print("{:d}".format(value))
        return True
    except Exception:
        return False
