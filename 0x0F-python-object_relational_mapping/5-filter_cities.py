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
    Query = "select cities.name as cities from cities\
                    inner join(states) on states.id = cities.state_id\
                    where states.name = %s\
                    order by cities.id asc;"
    db = MySQLdb.connect(host="localhost",
                         user=MY_USER, passwd=MY_PASS, db=MY_DB)

    cur = db.cursor()
    cur.execute(Query,(argv[4],))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end="")
        if i < len(rows) - 1:
            print(", ", end="")
        else:
            print()
