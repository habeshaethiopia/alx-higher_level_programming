#!/usr/bin/python3
#!/usr/bin/python3
"""the advanced task start module"""
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname)
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    conn = Session()
    result = conn.query(State).all()
    for s in result:
        for i in s.cities:
            if s.id == i.state_id:
                  print("{}: {} -> {}".format(i.id, i.name, s.name))
