#!/usr/bin/python3
""" contains the class definition of a State and 
    an instance Base = declarative_base()
"""
import SQLAlchemy
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """Our States ORM class"""
    __tablename__ = "states"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
