#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ope = ['+', '-', '/', '*']
    func = [add, sub, div, mul]
    if sys.argv[2] not in ope:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = func[ope.index(sys.argv[2])](int(sys.argv[1]), int(sys.argv[3]))
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, result))
