#!/usr/bin/python3
"""sql injection prevntion"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    MY_AEG = argv[4]
    Query = "select * from states where \
        name = \"{}\" \
                order by states.id asc;".format(MY_AEG)
    db = MySQLdb.connect(host="localhost",
                         user=MY_USER, passwd=MY_PASS, db=MY_DB)

    cur = db.cursor()
    cur.execute(Query)
    rows = cur.fetchall()
    tup = ()
    for row in rows:
        for col in row:
            tup = tup + (col,)
        print(tup)
        tup = ()
