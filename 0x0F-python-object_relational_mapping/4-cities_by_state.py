#!/usr/bin/python3
"""this module is for connecting to the mysql database and to print
what is inside the cities table and joins to states table using the
foreign key state id in cities table"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    Query = "select cities.id,cities.name as cities,states.name from cities\
                    inner join(states) on states.id = cities.state_id\
                    order by cities.id asc;"
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
