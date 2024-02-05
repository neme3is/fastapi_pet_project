import sqlalchemy
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = sqlalchemy.Column(Integer, primary_key=True)
    name = sqlalchemy.Column(String)
