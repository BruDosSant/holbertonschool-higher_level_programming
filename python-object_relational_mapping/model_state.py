#!/usr/bin/python3
"""State model for SQLAlchemy ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that maps to 'states' table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
