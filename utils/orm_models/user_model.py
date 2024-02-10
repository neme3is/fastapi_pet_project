import sqlalchemy
from sqlalchemy import Integer, String

from utils.orm_models.base_class_orm import Base


class User(Base):

    __tablename__ = 'Users'

    id = sqlalchemy.Column(Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(String)
