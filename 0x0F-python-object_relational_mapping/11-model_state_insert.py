#!/usr/bin/python3
"""script that adds the State object “Louisiana”
   to the database hbtn_0e_6_usa"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import exit, argv
from model_state import Base, State
from urllib.parse import quote_plus


if __name__ == "__main__":
    """prints the State object passed as argument from a database"""
    """lists all State objects from the database"""
    if (len(argv) < 4):
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    passwd_escaped = quote_plus(passwd)  # filterd/escaped special char '@'

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{\
}".format(user, passwd_escaped, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = State(name="Louisiana")
    session.add(new_city)
    print(new_city.id)
    session.commit()

    session.close()
