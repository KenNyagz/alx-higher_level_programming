#!/usr/bin/python3
"""script that prints the State object with the name passed as
   argument from the database hbtn_0e_6_usa"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import exit, argv
from model_state import Base, State
from urllib.parse import quote_plus


if __name__ == "__main__":
    """prints the State object passed as argument from a database"""
    """lists all State objects from the database"""
    if (len(argv) < 5):
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    passwd_escaped = quote_plus(passwd)  # filterd/escaped special char '@'
    state_name = (argv[4],)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{\
}".format(user, passwd_escaped, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
