#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv
if __name__=="__main__":
    res = requests.get(argv[1])
    page = res.json()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page.response))