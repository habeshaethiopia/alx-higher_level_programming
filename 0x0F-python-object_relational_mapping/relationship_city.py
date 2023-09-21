#!/usr/bin/python3
"""class definition of a City and an instance of Base"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """for state class"""

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False )
    state_id = Column(
        Integer, ForeignKey("states.id"), nullable=False
    )

    __tablename__ = "cities"
   