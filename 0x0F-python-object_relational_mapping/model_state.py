#!/usr/bin/python3
"""
script that put all states with a name starting N from database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

Base = declarative_base()


class State:
    """a python file that contains the class definition of a State"""

 __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    myFunction(argv[1], argv[2], argv[3])
