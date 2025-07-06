#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_6_usa using SQLAlchemy ORM"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            dbname
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
