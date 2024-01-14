#!/usr/bin/python3
""" contains the class definition of a State and 
    an instance Base = declarative_base()
"""
from SQLAlchemy import Column, Integer, String, create_engine
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy.orm import sessionmaker


Base = declarative_base()
class State(Base):
    """Our States ORM class"""
    __tablename__ = "states"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://root:@Kennyaga@localhost:3306/hbtn_0e_4_usa)')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
session = session()
