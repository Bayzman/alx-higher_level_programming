#!/usr/bin/python3

""" contains the class definition of a State and an \
instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """ contains the class definition of a State and an
        instance Base = declarative_base()
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
