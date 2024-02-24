#!/usr/bin/python3
"""
script that put all states with a name starting N from database hbtn_0e_0_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    new = create_new("mysql+mysqldb://{}:{}@localhost/{}"
                     .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                     pool_pre_ping=True)
    Session = sessionmaker(bind=new)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
