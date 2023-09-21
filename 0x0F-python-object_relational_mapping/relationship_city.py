#!/usr/bin/python3
"""class definition of a City and an instance of Base"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """for state class"""

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False )
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)