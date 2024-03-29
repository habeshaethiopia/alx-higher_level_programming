#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode("utf-8")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
