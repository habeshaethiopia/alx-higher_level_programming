#!/usr/bin/python3
"""displays the body of the response"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    res = request.Request(argv[1])
    try:
        ans = request.urlopen(res)
        print(ans.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
