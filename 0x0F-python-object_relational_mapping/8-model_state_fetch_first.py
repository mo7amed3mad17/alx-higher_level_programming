#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the database connection parameters from the command line
    un = sys.argv[1]
    pw = sys.argv[2]
    dn = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(f'mysql://{un}:{pw}@localhost:3306/{dn}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects and sort them by id
    states = session.query(State).order_by(State.id).first()

    # Print the results
    print(f"{states.id}: {states.name}")

    # Close the session
    session.close()
