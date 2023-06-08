#!/usr/bin/python3
from calculator_1 import *
import sys
sys.stderr.write("10 + 5 = {}\n".format(add(10, 5)))
sys.stderr.write("10 - 5 = {}\n".format(sub(10, 5)))
sys.stderr.write("10 * 5 = {}\n".format(mul(10, 5)))
sys.stderr.write("10 / 5 = {}\n".format(div(10, 5)))
