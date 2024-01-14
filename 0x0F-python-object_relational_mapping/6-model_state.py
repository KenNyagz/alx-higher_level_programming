#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from urllib.parse import quote_plus  # to escape special charct '@' in passwd
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    passwd = sys.argv[2]
    passwd_escaped = quote_plus(passwd)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], passwd_escaped, sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
