#!/usr/bin/python3
"""the orm implimentationl using sqlalchemy"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """for state class"""
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128))
    __tablename__ = "states"
