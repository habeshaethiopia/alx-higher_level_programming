#!/usr/bin/python3
"""the orm implimentationl using sqlalchemy"""
from sqlalchemy import ForeignKey, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """for state class"""

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128))
    state_id = Column(
        Integer, ForeignKey("State.id"), autoincrement=True, nullable=False
    )

    __tablename__ = "cities"
