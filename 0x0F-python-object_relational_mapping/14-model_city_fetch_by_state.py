#!/usr/bin/python3
"""using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import Base, City
from model_state import Base, State

if __name__ == "__main__":
    # Get input arguments
    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    # Create engine and session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname)
    )
    Session = sessionmaker(bind=engine)
    conn = Session()
    result = (
        conn.query(City, State)
        .join(State, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
