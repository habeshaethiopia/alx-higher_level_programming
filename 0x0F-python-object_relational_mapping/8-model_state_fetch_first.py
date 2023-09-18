#!/usr/bin/python3
"""using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).order_by(State.id).first()
    if i:
        print("{}: {}".format(i.id, i.name))
    else:
        print()
