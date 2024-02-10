import sqlalchemy
from sqlalchemy import Integer, String

from utils.orm_models.base_class_orm import Base


class Good(Base):

    __tablename__ = 'good'

    id = sqlalchemy.Column(Integer, primary_key=True)
    name = sqlalchemy.Column(String)

