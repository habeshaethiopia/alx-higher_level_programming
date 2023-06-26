#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
        if notisdigit(value):
            raise Exception
        return True
    except Exception:
        return False
