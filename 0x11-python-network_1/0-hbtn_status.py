#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

res = request.Request("https://alx-intranet.hbtn.io/status")
with request.urlopen(res) as response:
    page = response.read()
print("Body response:")
print("\t- type: {}".format(type(page)))
print("\t- content: {}".format(page))
print("\t- utf8 content: {}".format(page.decode("utf-8")))
