#!/usr/bin/python3
#!/usr/bin/python3
"""using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import Base, City   
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
    for i in session.query(City,State).join(City.state_id==State,State.id).all():
        print("{}: ({}) {}".format(State.name,i.id, i.name))