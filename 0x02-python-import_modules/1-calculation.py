#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == '__main__':
    print("{:d} + {:d} = {:d}".format(10, 5, add(a, b)))
    print("{:d} - {:d} = {:d}".format(10, 5, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(10, 5, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(10, 5, div(a, b)))
