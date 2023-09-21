#!/usr/bin/python3
"""the advanced task start module"""
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname)
    )
    Session = sessionmaker(bind=engine)
    conn = Session()
    S_add = State(name="California")
    conn.add(S_add)
    C_add = City(name="San Francisco" ,state = S_add)
    conn.add(C_add)
    conn.commit()
    conn.close()
