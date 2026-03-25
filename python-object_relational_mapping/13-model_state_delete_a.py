#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_to_find = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter(
        State.name.contains('a')).all()

    for state in states_to_delete:
        session.delete(state)

        session.commit()

        session.close()
